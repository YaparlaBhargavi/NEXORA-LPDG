\# AI Usage



\## How AI was used



AI was used as a development and analysis assistant during the challenge.



It helped with:



\- understanding the challenge requirements;

\- exploring the supplied datasets;

\- writing and debugging Python commands;

\- checking telemetry features;

\- comparing different scoring approaches;

\- analysing the trade-off between false visits and missed broken gateways;

\- creating validation and analysis scripts;

\- improving the explanation of the final Data Science approach;

\- preparing documentation such as DECISIONS.md.



The final decisions were based on analysis performed on the supplied challenge data.



\## One AI mistake that was caught



During development, an AI-generated command for comparing different score weightings contained a Python syntax error.



The command failed before producing any result. The error was identified from the terminal output, and the analysis was rerun using a simpler Python script.



This reinforced the need to verify AI-generated code by actually running it and checking the results rather than assuming that generated code is correct.



\## Human verification



All important outputs were checked by running the code locally.



The final predictions were checked for:



\- exactly 120 rows;

\- 15 gateways for each of the 8 weeks;

\- no duplicate gateway within a week;

\- valid ranking;

\- numeric scores;

\- non-empty reasons;

\- and compliance with the supplied submission validator.

