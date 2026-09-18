# Lab 2: Beacon on Pig Hill

|Item |       |
|:----|:------|
|Released |Week 4, Friday lecture |
|Due |See the [course schedule](https://computationalexpression.com/schedule/) |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

Everyone in Meadville knows Radio Tower Hill as Pig Hill, and the 2025 horror film *Pig Hill*
was built on the legend of what lives up there. Tonight you are alone at the top of it, keeping
the radio tower's red warning light lit. Your Raspberry Pi Pico 2 W's built-in LED is that light.
Every stage is a decision your program makes, and the light answers each one. No two nights on
the hill have to end the same way.

## Contents

* [Course learning outcomes](#course-learning-outcomes)
* [Meet the Pico 2 W](#meet-the-pico-2-w)
* [The four stages](#the-four-stages)
  * [The tower log](#the-tower-log)
  * [Expected output](#expected-output)
* [Getting started](#getting-started)
* [Evaluation](#evaluation)
  * [Programming, 3.0 points](#programming-30-points)
  * [Code quality and style, 1.0 point](#code-quality-and-style-10-point)
  * [Summary writing, 0.5 points](#summary-writing-05-points)
* [Code review](#code-review)
* [Submitting](#submitting)

## Course learning outcomes

This lab addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this lab you should be able to:

* control a physical device's output with `machine.Pin` and `time.sleep`
* choose the correct branch of an `if`/`else` based on a condition, and store a value inside it
* order an `if`/`elif`/`else` chain so that each branch can actually be reached
* join two conditions into one with `or`, and say when `and` would be wrong
* nest one `if` inside another, and explain what the indentation tells Python
* print a value three different ways: commas, `+` with `str()`, and an f-string

## Meet the Pico 2 W

Your Pico 2 W is a microcontroller, not a small computer: your program runs directly against
the hardware, with nothing in between. `Pin("LED", Pin.OUT)` gives you control of the board's
built-in LED; `led.on()` and `led.off()` send it 3.3V and 0V. See Week 4 Session 2's slides for
the fuller explanation of what is happening electrically.

**Setup, one time only:**

1. Install the **MicroPico** extension by **paulober** in VS Code, if you have not already
   (the steps are on the [Week 4 Session 2 slides](https://computationalexpression.com/slides/week-04-session-2/))
2. Open your `cmpsc100` folder in VS Code (File, then Open Folder). If you have not set up
   MicroPico in that folder yet: View, then Command Palette, type `MicroPico`, and choose
   **MicroPico: Initialize MicroPico Project**
3. Plug in your Pico 2 W over USB. The board shows no light of its own; that is normal
4. Confirm the bar along the bottom of the window reads **Pico Connected**

If it will not connect, ask an instructor or TL. Do not troubleshoot hardware alone the night
before it is due.

## The four stages

Everything this lab asks for is covered by Monday of Week 5. There is no loop anywhere in it:
each stage is a decision, and decisions are all you need.

**Stage One: Light the Tower.** Ask the user's name and whether to switch on the tower light now
that the sun is down. An `if`/`else` calls `led.on()` or `led.off()`, prints a message, and
records `LIT` or `DARK` for the log.

**Stage Two: The Wind Gauge.** A number the user types becomes one of four wind statuses through
an `if`/`elif`/`elif`/`else` chain. The order of that chain is what decides the result: a reading of
`180` is greater than every threshold in it, so the branch you write first is the branch that
claims it. The `CRITICAL` branch also flashes the light three times, the warning every driver in
Meadville knows.

**Stage Three: The Tree Line.** Two points of light blink on at the tree line below you, low to
the ground and too far apart to be a deer. Do they move when your light hits them? Do you hear
anything from the trees? Either sign on its own means you are not alone up here, so this is one
`if` whose condition joins the two answers with `or`. When it holds, you kill the light.

**Stage Four: The Ride Home.** Headlights flash from the bottom of the hill: your ride, asking
whether it is safe to come up. You can answer only when you know tonight's answer code *and* the
tower's backup battery holds at least 40 percent. Write this one as an `if` inside another `if`
rather than with `and`: the two ways it can go wrong deserve different endings (`STRANDED` when
the battery dies mid-code, `LEFT BEHIND` when you never knew the code), and a single `and` gives
both the same `else`. The indentation is the only thing that tells Python the battery check
belongs inside the code check.

### The tower log

The program ends with a log, and the automated checks read **only the log**, never the story.
Word every message above however you like. The log has six lines, in this order:

```text
TOWER LOG: JJ
==================================================
Tower light: LIT
Wind reading: CRITICAL
Tree line: NOT ALONE
Final status: PICKED UP
```

The status words are `LIT` or `DARK`; `CRITICAL`, `HIGH`, `STEADY`, or `CALM`; `NOT ALONE` or
`CLEAR`; `PICKED UP`, `STRANDED`, or `LEFT BEHIND`. Print each line any of the three ways from
Week 3: `print("Tree line:", tree_line)`, `print("Tree line: " + tree_line)`, or
`print(f"Tree line: {tree_line}")` all pass. The checks forgive extra spaces and letter case.

The checks type the answers in the order the starter asks them: name, tower light, wind
reading, moved, heard, answer code, battery. Keep the questions in that order.

### Expected output

One complete run, with `yes`, `180`, `yes`, `no`, `yes`, and `80` as the answers:

```text
==================================================
BEACON ON PIG HILL
==================================================
What is your name? JJ
The sun is down over Pig Hill. Switch on the tower light? (yes/no): yes
JJ, the tower light glows red over Meadville.

What does the tower's wind gauge read, in km/h? (0-200): 180
The tower groans in the gale. The light flashes the warning every driver in Meadville knows.

Two points of light blink on at the tree line, low to the ground and too far apart to be a deer.
Do they move when your light hits them? (yes/no): yes
Do you hear anything from the trees? (yes/no): no
You kill the light. Whatever is down there does not need to know where you are.

Headlights flash from the bottom of the hill: your ride, asking if it is safe to come up.
Do you know tonight's answer code? (yes/no): yes
Tower backup battery remaining, as a percentage? (0-100): 80
You flash the code, and the truck starts up the hill.

==================================================
TOWER LOG: JJ
==================================================
Tower light: LIT
Wind reading: CRITICAL
Tree line: NOT ALONE
Final status: PICKED UP
```

## Getting started

Open `src/main.py` and work through the `TODO` markers in order. Run it on your Pico as you go
by clicking **Run** in the bar along the bottom of the window, or from the terminal against a
plain Python interpreter for the parts that do not depend on real hardware timing:

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
| Programming | 3.0 | The 13 code checks below. Your score is the fraction passed, times 3.0 |
| Code quality and style | 1.0 | Descriptive names (0.3), clear organization (0.3), useful comments (0.4) |
| Summary writing | 0.5 | A complete, thoughtful `docs/summary.md` |
| **Total** | **4.5** | |

### Programming, 3.0 points

Run the checks yourself, as many times as you like, before you submit:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says what to look at when it fails. Thirteen of the checks are about
your code:

* the tower log names you, and the tower light logs `LIT` for `yes` and `DARK` for anything else
* a reading of `180` is `CRITICAL`, and readings of exactly `150`, `80`, `20`, and `5` land in
  the four statuses
* one sign at the tree line, by itself, logs `NOT ALONE`; no sign logs `CLEAR`
* with the code, the battery decides between `PICKED UP` and `STRANDED`; without the code, a
  full battery still logs `LEFT BEHIND`
* no `TODO` markers remain, there are at least six comments, one `if` joins two conditions with
  `or` or `and`, one `if` sits inside another, and neither `for` nor `while` appears anywhere

Partial credit is proportional: passing 10 of 13 checks earns `(10 ÷ 13) × 3.0 = 2.3` points.

The remaining two checks look at `docs/summary.md`. They confirm the document is finished, and
they count toward Summary writing below rather than toward these 3.0 points.

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

* why a reading of `180` reaches the branch you meant it to reach, and what a different ordering
  of that chain would do to it
* which runs of the program would end differently if the tree line's `or` were an `and`
* why the ride home is nested rather than written with `and`, and what changes if the inner `if`
  is unindented to sit beside the outer one

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
git commit -m "Complete the beacon on Pig Hill"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it (this is `git add`)
2. Type a message in the box at the top, then click the checkmark (this is `git commit`)
3. Click **Sync Changes** (or the &uarr; arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.
