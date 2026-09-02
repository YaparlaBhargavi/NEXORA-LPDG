import pandas as pd
from pathlib import Path

D = Path(r".\03-challenge-data\data")

files = list((D / "telemetry").glob("month=*/part-*.parquet"))

x = pd.concat(
    [
        pd.read_parquet(
            f,
            columns=[
                "gateway_id",
                "ts_utc",
                "disconnection_cnt",
                "no_conn_importance"
            ]
        )
        for f in files
    ],
    ignore_index=True
)

x["ts"] = pd.to_datetime(x["ts_utc"], utc=True)

weeks = pd.date_range("2026-02-02", periods=8, freq="7D")

print("WEEK        COMMON TOP15")

for week in weeks:

    end = pd.Timestamp(week, tz="UTC")
    start = end - pd.Timedelta(days=7)

    q = (
        x[(x["ts"] >= start) & (x["ts"] < end)]
        .groupby("gateway_id")
        .agg(
            dc=("disconnection_cnt", "sum"),
            nc=("no_conn_importance", "sum")
        )
        .reset_index()
    )

    q["dc_n"] = (
        (q["dc"] - q["dc"].min())
        / (q["dc"].max() - q["dc"].min())
    )

    q["nc_n"] = (
        (q["nc"] - q["nc"].min())
        / (q["nc"].max() - q["nc"].min())
    )

    q["score_7030"] = 0.7 * q["dc_n"] + 0.3 * q["nc_n"]

    top_7030 = set(
        q.nlargest(15, "score_7030")["gateway_id"]
    )

    top_nc = set(
        q.nlargest(15, "nc_n")["gateway_id"]
    )

    common = len(top_7030 & top_nc)

    print(week.strftime("%Y-%m-%d"), "     ", common)