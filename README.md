# Lab 2: Beacon

|Item |       |
|:----|:------|
|Released |Week 4, Friday lecture |
|Due |See the [course schedule](https://computationalexpression.com/schedule/) |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

Your Raspberry Pi Pico 2 W's built-in LED is a hilltop signal beacon, and you are its keeper
on the night a storm comes in. Every stage is a condition your program evaluates, and the beacon
answers with light each time. No two nights have to end the same way.

## Course learning outcomes

This lab addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this lab you should be able to:

* control a physical device's output with `machine.Pin` and `time.sleep`
* choose the correct branch of an `if`/`else` based on a condition
* order an `if`/`elif`/`else` chain so that each branch can actually be reached
* nest one `if` inside another, and explain what the indentation tells Python
* store a value inside a branch and use it after the branch has finished

## Meet the Pico 2 W

Your Pico 2 W is a microcontroller, not a small computer: your program runs directly against
the hardware, with nothing in between. `Pin("LED", Pin.OUT)` gives you control of the board's
built-in LED; `led.on()` and `led.off()` send it 3.3V and 0V. See Week 4 Session 2's slides for
the fuller explanation of what is happening electrically.

**Setup, one time only:**

1. Install the **MicroPico** extension by **paulober** in VS Code, if you have not already
   (the steps are on the [Week 4 Session 2 slides](https://computationalexpression.com/slides/week-04-session-2/))
2. Plug in your Pico 2 W over USB
3. Press `Ctrl/Cmd+Shift+P`, then run **MicroPico: Initialize MicroPico**
4. Confirm the bottom status bar reads **Pico Connected**

If it will not connect, ask an instructor or TL. Do not troubleshoot hardware alone the night
before it is due.

## The four stages

Everything this lab asks for was covered by the day it was released. There is no loop anywhere
in it: each stage is a decision, and decisions are all you need.

**Stage One: Light the Beacon.** Ask the keeper's name and whether to light the beacon now
that night has fallen, then use `if`/`else` to call `led.on()` or `led.off()` and print the
matching message.

**Stage Two: Aim the Beacon.** The beacon turns on its mount, and three directions are open. An
`if`/`elif`/`else` on the answer decides how many villages can see the light, and that number is
still there at the end of the program, in the keeper's log.

**Stage Three: The Wind Gauge.** A number the user types becomes one of four wind statuses
through an `if`/`elif`/`elif`/`else` chain. The order of that chain is the entire problem: a
reading of `180` is greater than every threshold in it, so the branch you write first is the
branch that claims it. The `CRITICAL` branch also flashes the beacon three times, the storm
warning every village knows.

**Stage Four: The Answering Light.** A light flickers on the far ridge, and the next keeper is
waiting. Your signal goes out only when you have tonight's signal code *and* the beacon holds at
least 40 percent charge. You have not been shown a way to write "and" yet, so write it as one
`if` inside another: the charge question is only worth asking once the code is in hand. The
indentation is the only thing that tells Python the second check belongs to the first.

### Expected output

One whole run, with `yes`, `north`, `180`, `yes`, and `80` as the answers:

```text
==================================================
BEACON
==================================================
Keeper, what is your name? JJ
Night has fallen. Light the beacon? (yes/no): yes
JJ, your beacon glows over the valley.
Beacon signal confirmed.

The beacon turns on its mount.
Which way do you aim it? (north/south/east): north
Three villages sit in the northern valley. All 3 see your light.

What does the wind gauge read, in km/h? (0-200): 180
The gale shakes the tower. Warn everyone below.

A light flickers on the far ridge. The next keeper is waiting.
Do you have tonight's signal code? (yes/no): yes
Beacon charge remaining, as a percentage? (0-100): 80
The code checks out, and your beacon blazes across the ridge.

==================================================
KEEPER'S LOG: JJ
==================================================
Aimed: north
Villages in sight: 3
Wind reading: CRITICAL
Final status: RELAYED
```

The narrative lines are yours to word. The log lines at the bottom, and the four status words
`CRITICAL`, `HIGH`, `STEADY`, and `CALM`, have to match exactly, because the automated checks
read them.

## Getting started

Open `src/main.py` and work through the `TODO` markers in order. Run it on your Pico as you go,
using MicroPico's **Run current file** command, or from the terminal against a plain Python
interpreter for the parts that do not depend on real hardware timing:

```text
uv run python src/main.py
```

> [!IMPORTANT]
> Run every command in this README from the assignment's **working directory**, the top-level
> folder you land in right after cloning, not from inside `src`.

## Evaluation

This lab is worth **4.5 points**, the standard value for a lab in this course.

| Component | Points | What it measures |
|:----------|:-------|:-----------------|
| Programming | 3.0 | The 18 code checks below. Your score is the fraction passed, times 3.0 |
| Code quality and style | 1.0 | Descriptive names (0.3), clear organization (0.3), useful comments (0.4) |
| Summary writing | 0.5 | A complete, thoughtful `docs/summary.md` |
| **Total** | **4.5** | |

### Programming, 3.0 points

Run the checks yourself, as many times as you like, before you submit:

```text
uv run gatorgrade --config gatorgrade.yml
```

Eighteen of the checks are about your code:

* the beacon lights for `"yes"` and stays dark for anything else
* each of the three directions produces the right number of villages
* each of the four wind statuses comes out of the right range, including exactly `80`
* the signal is relayed with the code and enough charge, fades with the code alone, and stays
  silent without the code no matter how full the beacon is
* no `TODO` markers remain, and neither the word `for` nor the word `while` appears anywhere

Partial credit is proportional: passing 15 of 18 checks earns `(15 ÷ 18) × 3.0 = 2.5` points.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

### Code quality and style, 1.0 point

Graded by a human reading your code. Descriptive variable names, sensible organization, and
comments that explain **why** rather than restating what the line already says.

### Summary writing, 0.5 points

Complete [`docs/summary.md`](docs/summary.md). Every question answered fully. Minimum word
count is `150`.

## Code review

A Technical Leader or the instructor will conduct a code review with you on this lab. **Code
reviews are graded separately from the 4.5 points above**, under the Code Reviews category on
the syllabus.

Two things happen, with you present:

1. **You run your program** on your Pico for the reviewer
2. **You answer questions about your own code**, including the concepts behind it

The reviewer opens a **Code Review** issue on your repository and fills it out during the
conversation. Come prepared to explain:

* how the `if`/`else` decided whether the beacon lit or stayed dark
* why a reading of `180` reaches the branch you meant it to reach, and what a different ordering
  of that chain would do to it
* what the indentation of the answering light's inner `if` tells Python, and what changes if
  those two checks sit side by side instead

**Your review must be completed during the lab session on the day this lab is due.** If you
cannot attend that lab and complete your review then, make arrangements to complete it
beforehand at office hours:

* **Technical Leaders**, listed on the calendar at
  [cis.allegheny.edu/community/news](https://www.cis.allegheny.edu/community/news/)
* **Dr. Jumadinova**, [book a time](https://janyljumadinova.com/office-hours/). Drop-ins are welcome
  during posted hours, but students who booked are seen first

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded. If you need more time, apply a late token with
[this form](https://forms.gle/3nGbpaNrG96DpLLdA).

**In the terminal:**

```text
git add src/main.py docs/summary.md
git commit -m "Complete the beacon"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it (this is `git add`)
2. Type a message in the box at the top, then click the checkmark (this is `git commit`)
3. Click **Sync Changes** (or the &uarr; arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.
