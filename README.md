# Make the AI Judge Laugh: the Office Joke Open

[![Bounty](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/cervus-snoopy/calm-fern-ledger-7q2m/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/cervus-snoopy/calm-fern-ledger-7q2m/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

This program writes a single original one-line joke about office life to `entry.txt`.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Verify

```sh
wc -c /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```

The entry must be one line, 1–200 characters, UTF-8, with no trailing newline, and the written file is re-read by the program itself to confirm its contents.
