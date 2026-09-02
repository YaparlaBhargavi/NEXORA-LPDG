\# NEXORA 2026 – LPDG Gateway Visit Prioritization



\## Project Overview



This project prioritizes 15 gateways for weekly field visits from approximately 320 gateways.



The system uses telemetry available before each prediction Monday and produces a ranked list of 15 gateways with a risk score and an explanation.



\## Objective



For each of the 8 challenge weeks, identify the 15 gateways that should receive a field visit and rank them from highest to lowest priority.



The 15-visit limit is treated as a hard operational constraint.



\## Prediction Weeks



The solution generates predictions for:



\- 2026-02-02

\- 2026-02-09

\- 2026-02-16

\- 2026-02-23

\- 2026-03-02

\- 2026-03-09

\- 2026-03-16

\- 2026-03-23



The final output contains 120 rows: 15 gateways × 8 weeks.



\## Method



The final solution uses a transparent composite risk score.



\### Recent 7-day signals



For each gateway, we calculate:



1\. Total disconnection count

2\. Total no-connection importance



Both signals are normalized across gateways for that prediction week.



\### Final score



The score is:



&#x20;   70% × normalized disconnection count

&#x20;   +

&#x20;   30% × normalized no-connection importance



Gateways are sorted by this score and the top 15 are selected.



\## Why this method?



Disconnection count directly represents reliability events.



No-connection importance provides an additional signal describing connection-related severity.



We tested alternative weightings. The historical engineer-review analysis showed that no-connection importance alone had slightly higher AUC than disconnection count alone, but different weightings produced highly similar top-15 lists.



The 70/30 combination was therefore retained because it combines two meaningful signals while remaining simple and explainable.



\## Data Leakage Prevention



For each prediction Monday, only telemetry with timestamps strictly before that Monday is used.



The scoring window is the 7 days immediately preceding the prediction Monday.



No future-week telemetry is used to generate a prediction.



\## Data Science Analysis



The Data Science analysis considers the operational costs:



\- €380 for a wrong visit

\- €600 for leaving a broken gateway unattended for one week



Fixed thresholds were tested to understand the trade-off between unnecessary visits and potentially missed broken gateways.



Because the field team has a hard limit of 15 visits, the final decision uses ranking rather than a fixed threshold.



See `DATA\_SCIENCE\_ANALYSIS.md` for the detailed analysis.



\## Validation



The final predictions are checked using the supplied challenge validator.



The output must contain:



\- exactly 120 rows;

\- 8 prediction weeks;

\- 15 gateways per week;

\- ranks 1–15;

\- no duplicate gateway within a week;

\- valid gateway IDs;

\- numeric scores;

\- non-empty reasons.



\## Files



\### Main files



\- `create\_predictions.py` – generates the final predictions

\- `predictions.csv` – final 120-row submission

\- `validate\_submission.py` – supplied validation script

\- `predictions\_baseline.csv` – supplied baseline result

\- `baseline\_3sigma.py` – supplied baseline implementation

\- `DECISIONS.md` – important project decisions and alternatives

\- `DATA\_SCIENCE\_ANALYSIS.md` – cost and threshold analysis

\- `AI-USAGE.md` – documentation of AI assistance and verification



\## Limitations



The available engineer review is a limited labelled sample and cannot be treated as complete ground truth for all gateways and all prediction weeks.



The final ranking can therefore still contain false visits or miss a gateway that later proves to be broken.



Additional weeks of prediction-versus-field outcomes would allow the score weights and operational cost estimates to be recalibrated using more evidence.



\## Running the solution



From the project root:



```text

python create\_predictions.py

