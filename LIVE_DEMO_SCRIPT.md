# NEXORA 2026 - Live Demo Speaking Script

## 0:00-0:45 - Problem
Our problem is to decide which 15 gateways should receive field visits every week.
There are approximately 320 gateways, but the field team can visit only 15.
So this is a prioritization problem under a hard operational constraint.

## 0:45-1:30 - Decision Definition
I define a gateway as needing a visit when it is among the top 15 gateways with the highest estimated reliability risk.
I use ranking instead of a fixed threshold because the number of visits must remain exactly 15.

## 1:30-2:30 - Data and Leakage Prevention
I use telemetry available before each prediction Monday.
The main scoring window is the most recent 7 days.
I use two signals: disconnection count and no-connection importance.
No future telemetry is used for the prediction.

## 2:30-3:30 - Risk Score
Both signals are normalized across gateways for each week.
The final score gives 70 percent weight to disconnection count and 30 percent to no-connection importance.
Higher score means higher estimated reliability risk.
The gateways are sorted by score and the top 15 are selected.

## 3:30-4:30 - Why This Method
I tested alternative approaches and weightings.
No-connection importance alone had slightly better historical AUC, but different weightings produced very similar top-15 lists.
Therefore I kept the 70-30 score because it combines two meaningful signals and remains transparent and easy to modify.

## 4:30-5:15 - Cost Decision
The challenge gives a cost of 380 euros for a wrong visit and 600 euros when a broken gateway is left unattended for one week.
A higher threshold reduces visits but can increase missed broken gateways.
A lower threshold does the opposite.
Because 15 visits is a hard limit, the final operational decision is still top 15 rather than a fixed threshold.

## 5:15-6:00 - Validation
The final submission contains 120 rows.
That is 15 gateways for each of the 8 challenge weeks.
The supplied validator reports OK.
I also checked that there are no duplicate gateways within a week and that the ranking and scores are valid.

## 6:00-6:45 - Live Change
If I move the risk threshold upward, fewer gateways are selected and the potential missed-gateway cost increases.
If I move it downward, more gateways are considered risky and unnecessary visits can increase.
This demonstrates that the threshold is a business trade-off, not simply a technical parameter.

## 6:45-7:30 - Limitations and Next Two Weeks
The engineer review is a limited labelled sample and historical field visits were not a random sample of the fleet.
So I do not claim that the current results are complete ground truth.
Another two weeks of actual prediction-versus-field outcomes would let us measure false visits, missed broken gateways, real weekly cost, and whether the score weights should change.

## Closing
The final solution is intentionally simple.
It converts recent reliability telemetry into a transparent risk ranking and gives the operations team exactly the 15 gateways they can visit.
