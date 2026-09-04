\# Decisions



\## 1. What does "needs a visit" mean?



We define a gateway as needing a visit when it is among the top 15 gateways with the highest estimated reliability risk for that week. The decision is primarily an early-warning choice: we are prioritising gateways showing evidence that they may fail or become unreliable, rather than waiting until a gateway is certainly broken. This is consistent with the economics because an unattended fault costs €600 for every week it remains unresolved.



We use a ranking rather than a fixed yes/no threshold because the field team has a hard limit of exactly 15 visits per week.



Alternative rejected:

A fixed risk threshold was tested, but it did not consistently produce an appropriate number of gateways across different weeks. Therefore, ranking the gateways and selecting the top 15 is more suitable for the operational constraint.



\---



\## 2. Which time window should be used?



We use telemetry from the most recent 7 days before each Monday to calculate the weekly risk score.



The data is strictly limited to timestamps before the prediction week's Monday, so information from the future is not used.



Alternative rejected:

Using only the most recent few hours or one day would be more reactive but would also be more sensitive to short-term noise. A 7-day window provides a more stable weekly signal.



\---



\## 3. How is the risk score calculated?



The final score is a transparent composite:



\- 70% normalized disconnection count

\- 30% normalized no-connection importance



Both signals are calculated over the recent 7-day window.



The score is used consistently to rank gateways from highest to lowest risk.



Alternative rejected:

The supplied 3-sigma baseline was useful as a reference, but it counts extreme hourly observations rather than directly combining the strongest reliability signals found during analysis.



\---



\## 4. Why use 70/30 weighting?



Disconnection count was given the larger weight because it directly represents backhaul disconnection events. No-connection importance was included as a secondary severity signal.



Historical analysis showed that no-connection importance alone had slightly better AUC than disconnection count alone. However, different weightings produced very similar top-15 gateway lists. For the Feb 16 reviewed week, all tested weightings identified the same 11 known Schlecht gateways in the top 15.



Across the eight prediction weeks, the 70/30 and no-connection-only top-15 lists had an average overlap of about 12 out of 15 gateways.



Therefore, we kept the 70/30 composite because it combines two meaningful signals while remaining simple and explainable.



Alternative rejected:

A more complicated model was not selected because the additional complexity did not clearly provide a better operational decision.



\---



\## 5. Which Part 2 area did we choose?



We selected the Data Science track.



We chose Data Science because the main challenge is a decision problem: selecting 15 gateways from approximately 320 gateways while balancing the cost of unnecessary visits against the cost of leaving a broken gateway unattended.



The solution therefore focuses on:



\- defining what "needs a visit" means;

\- testing alternative definitions;

\- evaluating the signals honestly;

\- considering uncertainty and limitations;

\- translating the €380 false-visit cost and €600 weekly missed-broken-gateway cost into decisions;

\- and explaining the result in a way an operations manager can understand.



Alternative rejected:

Other tracks such as Machine Learning could support a more complex predictive model, but ML is not required by the challenge and a transparent ranking method is easier to validate, explain and modify during the live session.



\---



\## Cost and threshold analysis



The challenge specifies:



\- €380 cost for a wrong visit;

\- €600 cost when a broken gateway is left unattended for one week;

\- 15 visits is the hard weekly limit.



We tested fixed score thresholds to understand the trade-off.



The analysis showed that increasing the threshold reduces the number of selected gateways but increases the number of potentially missed gateways.



For example, in the reviewed sample:



| Threshold | Selected | Confirmed Schlecht | Potential missed | Estimated cost |

|---:|---:|---:|---:|---:|

| 0.10 | 14 | 13 | 39 | €23,780 |

| 0.20 | 9 | 9 | 43 | €25,800 |

| 0.30 | 7 | 7 | 45 | €27,000 |

| 0.50 | 4 | 4 | 48 | €28,800 |

| 0.70 | 1 | 1 | 51 | €30,600 |



These threshold results are based on the available reviewed sample and should not be interpreted as a complete estimate for all gateways or all weeks.



Because the field operation has a hard limit of 15 visits, the final system uses ranking rather than applying a fixed threshold.



\---



\## Limitations



The engineer review contains only a limited labelled sample, so the observed performance cannot be assumed to represent every gateway or every future week.



The top-15 list can contain gateways that later turn out to be normal, and a broken gateway can be missed because only 15 visits are possible.



The current score is intentionally transparent rather than a complex predictive model.



Another two weeks of observed field outcomes would allow us to compare predictions with actual outcomes, estimate false-visit and missed-broken costs more reliably, and reconsider the score weights using additional evidence.



