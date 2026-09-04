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

During development, an AI-generated Windows command was intended to create the `.gitignore` file, but the resulting file did not contain the intended ignore rules cleanly. This was caught by inspecting the actual `.gitignore` contents and then checking whether a real telemetry `.parquet` file was ignored with `git check-ignore`.

The problem was corrected by rewriting `.gitignore` and verifying that the challenge data was not tracked by Git. A final `git status` and `git ls-files` check confirmed that the dataset was excluded from the repository.

This showed why AI-generated commands must be checked against their actual effect, especially for repository and data-safety operations.

## Human verification



All important outputs were checked by running the code locally.



The final predictions were checked for:



\- exactly 120 rows;

\- 15 gateways for each of the 8 weeks;

\- no duplicate gateway within a week;

\- valid ranking;

\- numeric scores;

\- non-empty reasons;

\- and compliance with the supplied submission validator.

