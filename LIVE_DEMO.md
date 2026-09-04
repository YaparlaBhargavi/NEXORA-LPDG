# NEXORA 2026 - Live Demo Plan

## 1. Problem
Select the 15 gateways that should receive field visits each week from approximately 320 gateways.

## 2. Operational Constraint
The field team can visit exactly 15 gateways per week.

## 3. Final Method
Use the most recent 7 days before Monday.
Combine normalized disconnection count at 70% and normalized no-connection importance at 30%.
Rank all gateways by the composite score and select the top 15.

## 4. Why This Method
The method is simple, transparent and easy to explain.
Disconnection count represents reliability events.
No-connection importance adds a second connection-severity signal.

## 5. Validation
The final predictions contain 120 rows: 15 gateways for each of 8 weeks.
The supplied challenge validator reports OK.

## 6. Live Change
Move the risk-score threshold and explain the cost trade-off.
A higher threshold means fewer visits but potentially more missed broken gateways.
A lower threshold means more gateways considered risky but potentially more unnecessary visits.
The final operational rule remains top-15 because 15 visits is a hard limit.

## 7. What Another Two Weeks Would Give Us
Two additional weeks of actual field outcomes would allow measurement of false visits and missed broken gateways.
It would also allow better estimation of weekly cost and recalibration of score weights.

## 8. Key Limitation
Historical engineer reviews and field visits are limited samples and cannot be treated as complete ground truth for the whole fleet.
