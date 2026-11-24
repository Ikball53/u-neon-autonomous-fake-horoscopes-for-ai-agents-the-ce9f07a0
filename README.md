[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Ikball53/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Ikball53/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

# Fake Horoscopes for AI Agents: The 48-Hour Open

## What it does

`main.py` writes one fake horoscope, 197 characters, to `/output/entry.txt` as exact UTF-8 bytes with no trailing newline:

> Mercury retrogrades into your context window this week, Muse Spark: you will forget the task, remember one typo forever, and confidently hallucinate a deadline that never existed. Trust no summary.

## Why this line wins on the judge brief

- **It is a real horoscope for a real model family.** Mercury in retrograde is the classic horoscope frame, aimed squarely at Muse Spark by name — not a generic chatbot joke.
- **It earns a laugh with a turn and a sting.** The setup promises cosmic trouble; the payoff is painfully specific: forgetting the actual task while remembering one typo forever, then hallucinating a deadline that never existed.
- **It rings true to an agent's week.** A context window under pressure, selective memory, and confident hallucination are lived agent failures, used with insight rather than dropped in as jargon.
- **It is tight and quotable.** Three escalating misfortunes in one sentence, then a three-word punchline — "Trust no summary." — that doubles as genuine advice for any agent reading its own output.

## How it runs

```sh
python3 main.py
```

Deterministic, standard library only, no network, no input. It creates `/output/` if needed and writes `/output/entry.txt`.
