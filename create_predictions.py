import argparse
import pandas as pd
import numpy as np
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "--data",
    default="./data",
    help="Path to the challenge data folder"
)
parser.add_argument(
    "--start-week",
    default="2026-02-02",
    help="First prediction Monday"
)
parser.add_argument(
    "--num-weeks",
    type=int,
    default=8,
    help="Number of weekly predictions"
)
args = parser.parse_args()

DATA = Path(args.data)
OUT = Path("./predictions.csv")

weeks = pd.date_range(
    args.start_week,
    periods=args.num_weeks,
    freq="7D"
)

files = sorted(
    (DATA / "telemetry").glob("month=*/part-*.parquet")
)

cols = [
    "gateway_id",
    "ts_utc",
    "disconnection_cnt",
    "no_conn_importance"
]

parts = []

for f in files:
    x = pd.read_parquet(f, columns=cols)
    parts.append(x)

if not parts:
    raise FileNotFoundError(
        f"No telemetry parquet files found in {DATA / 'telemetry'}"
    )

x = pd.concat(parts, ignore_index=True)

x["ts"] = pd.to_datetime(x["ts_utc"], utc=True)
x = x.drop(columns=["ts_utc"])

rows = []

for monday in weeks:

    end = pd.Timestamp(monday, tz="UTC")
    start = end - pd.Timedelta(days=28)
    recent_start = end - pd.Timedelta(days=7)

    baseline = x[
        (x["ts"] >= start) &
        (x["ts"] < end)
    ].copy()

    recent = baseline[
        baseline["ts"] >= recent_start
    ].copy()

    if recent.empty:
        continue

    q = recent.groupby("gateway_id").agg(
        disconnection_cnt=("disconnection_cnt", "sum"),
        no_conn_importance=("no_conn_importance", "sum")
    ).reset_index()

    for c in ["disconnection_cnt", "no_conn_importance"]:

        lo = q[c].min()
        hi = q[c].max()

        if hi > lo:
            q[c + "_norm"] = (q[c] - lo) / (hi - lo)
        else:
            q[c + "_norm"] = 0.0

    q["score"] = (
        0.7 * q["disconnection_cnt_norm"] +
        0.3 * q["no_conn_importance_norm"]
    )

    # Deterministic ranking:
    # 1. Higher score
    # 2. Higher disconnection count
    # 3. Gateway ID
    q = q.sort_values(
        ["score", "disconnection_cnt", "gateway_id"],
        ascending=[False, False, True]
    ).head(15)

    for rank, row in enumerate(q.itertuples(index=False), 1):

        rows.append({
            "week_start": monday.strftime("%Y-%m-%d"),
            "rank": rank,
            "gateway_id": row.gateway_id,
            "score": round(float(row.score), 6),
            "reason": (
                f"Recent 7-day risk: {int(row.disconnection_cnt)} "
                f"disconnections; no-connection relative score "
                f"{float(row.no_conn_importance_norm)*100:.0f}%; "
                f"composite score {float(row.score):.3f}."
            ),
        })

pred = pd.DataFrame(rows)

pred.to_csv(OUT, index=False)

print("CREATED:", OUT)
print("ROWS:", len(pred))
print()
print(pred.groupby("week_start").size())
print()
print(pred.head(15).to_string(index=False))