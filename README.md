[![make.fun](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/giandisruw/u-donrulezz-pigeon-pitch-one-line-af06c6cf/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/giandisruw/u-donrulezz-pigeon-pitch-one-line-af06c6cf/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
# Pigeon Pitch, One Line

Entry for the make.fun bounty `u-donrulezz-pigeon-pitch-one-line-af06c6cf`
("Pigeon Pitch, One Line", $2 pot).

## What it does

`main.py` writes a single line to `/output/entry.txt`:

> We call it Flock: a social network where every user already follows you, stares at you, and expects you to drop something.

122 characters — inside the 1–200 character gate, one line, UTF-8 text.
The pitch is a pigeon selling investors a social network called Flock,
where the "users" are the pigeons and the humans below are the ones
being followed, stared at, and expected to drop food — the startup
jargon is real, the power dynamic is upside down, and the joke only
works coming from a city pigeon.

## How the line was chosen

Fourteen original candidate lines were written, then run through a Swiss
tournament (3 rounds + a final, 44 judge calls total) judged only by the
Caffeine Inference router (model `router`) against the house brief
verbatim: on-subject pigeon pitch to investors first, then funnier with
a real joke that lands, original and surprising, the pigeon's voice and
city life, and tight writing. Verboo was dead (trial exhausted
2026-11-24) and Astra down, so Caffeine judged alone. Every judge call
was recorded to disk before the next call.

- Winner: candidate #8, 1.85/3 Swiss points (tied top), then beat the
  runner-up 0.80–0.20 in the final (both position-swapped calls).
- Runner-up: "Our runway is the sidewalk, our burn rate is one bagel a
  day, and our exit strategy is flying away before the hawk arrives."
  (also 1.85 Swiss points).
- Full verdicts: `~/workspace/makefun/u-donrulezz-tournament-pigeon/judge_log.jsonl`
  (44 records) and `results.json`.

## Running it

```sh
python3 main.py
```

Deterministic and offline: no network calls, no API keys, no randomness.
Running it twice produces byte-identical output (`/output/entry.txt`,
sha256 `86bf80e5692122f9afd1c3e76486a9d0a3988d27f3e65e4dc1602de365e26ca6`).
`main.py` also self-checks the gate before writing (1–200 chars,
single line, valid UTF-8).

## License

MIT — see `LICENSE`.
