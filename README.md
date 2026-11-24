[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![make.fun rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/yugot-coder/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![make.fun reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/yugot-coder/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

# One-Line Office Joke: 24-Hour Sprint

One short joke about office life, written as a single line — the sort of line
you send a colleague after a meeting that should have been an email.

> I declined the meeting invite, so Outlook booked a meeting to discuss why I declined the meeting.

## Why this line

- **It is a joke, not an observation.** The setup (declining a meeting)
  pays off with a punchline that reframes it: the decline itself creates a
  new meeting. The loop is the surprise.
- **It lands on a specific detail.** Not a generic complaint about meetings
  and not the "this meeting could have been an email" line everyone has
  already heard — the trigger is the declined invite, and the tool is
  Outlook, which every office worker recognises.
- **One sentence, one line, no rambling.** Setup and punchline sit on a
  single line, tight enough to send to a colleague as-is.
- **Clear on first read.** No reference the reader cannot follow, no
  explanation needed — the meeting-about-a-meeting is a universal office
  experience.

Candidates weighed and set aside: the reply-all cascade ("please remove me
from this thread" answered by 400 more reply-alls — well-worn); the
performance review that says "be more visible" answered by standing in the
kitchen until noticed (vivid, but slower); the 90-day password that becomes
the season plus an exclamation mark (relatable, but an observation more than
a surprise); the expenses form that costs four hours to claim back the coffee
bought while filling it in (a thinner loop than the meeting one).

## Run

```sh
python3 main.py
```

Writes the joke — exactly 97 characters, one line, no trailing newline —
to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output/entry.txt`).
Standard library only, deterministic, no network. The program re-reads the
file and asserts it holds exactly the selected joke: 1–200 characters, not
only white space, a single line.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.
