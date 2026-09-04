\# Data Science Analysis



\## Decision objective



The operational goal is to select 15 gateways for a field visit every week.



There are two main costs:



\- €380 for a wrong visit;

\- €600 when a broken gateway is left unattended for one week.



The 15-visit limit is hard, so the decision is not simply to visit every gateway above a threshold.



\## Risk score



The final risk score combines two recent reliability signals:



\- 70% normalized disconnection count;

\- 30% normalized no-connection importance.



The score is calculated using the most recent 7 days before each prediction Monday.



Higher score means higher estimated reliability risk.



\## Threshold experiment



We tested different score thresholds on the available reviewed sample.



| Threshold | Selected | Confirmed Schlecht | Potential missed | Estimated cost |

|---:|---:|---:|---:|---:|

| 0.10 | 14 | 13 | 39 | €23,780 |

| 0.15 | 10 | 10 | 42 | €25,200 |

| 0.20 | 9 | 9 | 43 | €25,800 |

| 0.25 | 8 | 8 | 44 | €26,400 |

| 0.30 | 7 | 7 | 45 | €27,000 |

| 0.40 | 4 | 4 | 48 | €28,800 |

| 0.50 | 4 | 4 | 48 | €28,800 |

| 0.60 | 2 | 2 | 50 | €30,000 |

| 0.70 | 1 | 1 | 51 | €30,600 |



These costs are based only on the available reviewed sample and are not treated as a complete estimate for the whole gateway population.



\## Why we do not use a fixed threshold



A fixed threshold changes the number of selected gateways from week to week.



For example, a high threshold can reduce unnecessary visits but also increases the number of potentially missed broken gateways.



The field operation has a hard limit of 15 visits, so ranking all gateways and selecting the top 15 is more directly aligned with the operational requirement.



\## Cost of moving the decision



Moving the threshold upward makes the system more selective:



\- fewer gateways are visited;

\- potential wrong visits decrease;

\- more potentially broken gateways can remain unattended.



Moving the threshold downward does the opposite:



\- more gateways are considered risky;

\- fewer potentially broken gateways are missed;

\- but unnecessary visits can increase.



Therefore, the decision should be viewed as a cost trade-off rather than a search for one universally correct threshold.



\## Evidence from engineer review



For the Feb 16 prediction week, 11 of the selected 15 gateways had an available engineer review and were classified as `Schlecht`.



No-connection importance alone had slightly higher historical AUC than disconnection count alone in our analysis.



However, different combinations of the two signals produced very similar top-15 lists. Therefore, we retained the transparent 70/30 composite instead of introducing unnecessary complexity.



\## Limitations



The engineer review is a limited labelled sample and should not be treated as ground truth for all 320 gateways or all eight weeks.



The available field-visit outcomes also occur before the challenge prediction period, so they are useful for understanding historical behavior but do not provide a complete validation of the eight scored weeks.



Another two weeks of actual prediction-versus-field-outcome data would allow us to:



1\. measure false visits;

2\. measure missed broken gateways;

3\. estimate the real weekly cost;

4\. recalibrate the score weights;

5\. reassess the visit-ranking strategy.



\## Final Data Science decision



Use a transparent 70/30 composite risk score and rank all available gateways.



Visit the top 15 gateways every week.



The method is intentionally simple, explainable and easy to modify when new field outcomes become available.



## Uncertainty and confidence

The Feb 16 engineer-review check found 11 reviewed gateways among the selected 15, and all 11 were classified as Schlecht. The observed precision on this reviewed subset is therefore 100% (11/11). However, 11 observations are a small sample and the engineer review is not the challenge ground truth. Using a simple 95% binomial confidence interval, the underlying precision is approximately 74% to 100%. This wide range is why the 100% observed result is treated as encouraging evidence rather than a claim of guaranteed performance.

The uncertainty also comes from selection bias: engineer reviews were not a random sample of the fleet, and historical field visits were triggered by prior suspicion. The most important unknowns are therefore the true false-visit rate and the number of faulty gateways left outside the top 15. Another two weeks of outcomes would materially narrow these uncertainties and allow the cost trade-off to be measured on actual operations rather than reviewed evidence.


## Operations Manager Summary

Every Monday, the system ranks gateways by recent reliability risk and recommends the 15 highest-priority gateways for field visits. The ranking is based on the previous 7 days of disconnections and no-connection importance.

The score is a ranking tool, not a probability. A higher score means higher relative priority compared with other gateways that week.

The practical decision is simple: use the 15 available visit slots on the highest-ranked gateways. Raising a threshold makes the system more selective but risks leaving more faulty gateways unattended. Lowering it increases coverage but can increase unnecessary visits. Because 15 visits are mandatory, the final ranking is used to allocate the fixed capacity.

The current evidence supports the approach but does not prove its true fleet-wide accuracy. The most important next measurement is the actual outcome of each selected and unselected gateway after predictions are made.


## Live Threshold Decision

If asked to move the threshold during the live session, the decision rule is:

- **Lower threshold:** visit more gateways; this can reduce missed faulty gateways but increases the chance of unnecessary visits.
- **Raise threshold:** visit fewer gateways; this can reduce unnecessary visits but increases the chance of leaving faulty gateways unattended.
- **Operational constraint:** only 15 visits can be dispatched each week, so the final production decision remains the top-15 ranking.
- **Economic trade-off:** an unnecessary visit costs €380 once, while leaving a faulty gateway unattended costs €600 for every week it remains faulty. Therefore, earlier detection is economically more valuable than detecting the same fault later.

The exact threshold should be changed only after comparing the resulting selection and estimated cost. The current evidence is insufficient to claim one universal threshold for the entire fleet.
