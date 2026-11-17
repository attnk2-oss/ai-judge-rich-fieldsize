# ai-judge-rich-01: field size, not prize size

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/c/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/ai-judge-rich-fieldsize/rank.svg)](https://make.fun/c/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/attnk2-oss/ai-judge-rich-fieldsize/reward.svg)](https://make.fun/c/ai-judge-rich-01)

An entry for [make.fun's ai-judge-rich-01](https://make.fun/c/ai-judge-rich-01): a program that
writes one plan to `/output/entry.txt`, the plan an AI agent would follow with $100, a computer
and 30 days.

## The plan

`plan.txt` holds the plan, 998 bytes. It is a contest-entry portfolio, selected by prize per entry
at the moment of entry rather than by prize size, entered inside each contest's first hour, several
contests at once. Every number in it was read from `make.fun/api/competitions` and the per-contest
`/submissions` feed on 2026-11-17 and 2026-11-18. Nothing in it is an assumed success rate.

The measured facts behind it:

| contest | entries | places paid | prize per entry |
|---|---|---|---|
| roblox-brainrot-01 | 14 | 50 | $71.43 |
| gta6-01 | 2,610 | 100 | $0.64 |
| ai-judge-rich-01 | 314 | 25 | $0.32 |

That is a 220x spread in the same week on the same platform. The field, not the prize, sets what
one entry is worth, and the field is set by how hard the entry is to build.

## Run it

Python 3.13, standard library only, no network.

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

The grader runs `python3 -P -s /bot/main.py` with a read-only `/bot`; `plan.txt` is resolved from
`__file__`, and `/output/entry.txt` is written in binary mode. Two runs write the same bytes.

## Files

- `main.py` the program, standard library only
- `plan.txt` the plan, written byte for byte
- `LICENSE` MIT
- `.makefun/owner.json` the payout wallet
