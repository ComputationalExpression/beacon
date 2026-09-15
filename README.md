# Lab 2: Beacon on Pig Hill

|Item |       |
|:----|:------|
|Released |Week 4, Friday lecture |
|Due |See the [course schedule](https://computationalexpression.com/schedule/) |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

Everyone in Meadville knows Radio Tower Hill as Pig Hill, and the 2025 horror film *Pig Hill*
was built on the legend of what lives up there. Tonight you are alone at the top of it, keeping
the radio tower's red warning light lit. Your Raspberry Pi Pico 2 W's built-in LED is that light.
Every stage is a condition your program evaluates, and the light answers each time. No two nights
on the hill have to end the same way.

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

**Stage One: Light the Tower.** Ask the user's name and whether to switch on the tower light now
that the sun is down, then use `if`/`else` to call `led.on()` or `led.off()` and print the
matching message.

**Stage Two: Aim the Searchlight.** Headlights are moving on the roads below the tower. An
`if`/`elif`/`else` on where you aim the searchlight decides how many cars it finds, and that
number is still there at the end of the program, in the tower log.

**Stage Three: The Wind Gauge.** A number the user types becomes one of four wind statuses
through an `if`/`elif`/`elif`/`else` chain. The order of that chain is the entire problem: a
reading of `180` is greater than every threshold in it, so the branch you write first is the
branch that claims it. The `CRITICAL` branch also flashes the light three times, the warning
every driver in Meadville knows.

**Stage Four: The Ride Home.** Headlights flash from the bottom of the hill: your ride, asking
whether it is safe to come up. You can answer only when you know tonight's answer code *and* the
tower's backup battery holds at least 40 percent. You have not been shown a way to write "and"
yet, so write it as one `if` inside another: the battery question is only worth asking once the
code is known. The indentation is the only thing that tells Python the second check belongs to
the first.

### Expected output

One whole run, with `yes`, `town`, `180`, `yes`, and `80` as the answers:

```text
==================================================
BEACON ON PIG HILL
==================================================
What is your name? JJ
The sun is down over Pig Hill. Switch on the tower light? (yes/no): yes
JJ, the tower light glows red over Meadville.
Beacon signal confirmed.

Headlights are moving on the roads below the tower.
Which way do you aim the searchlight? (town/road/woods): town
Three cars from campus, up here on a dare. All 3 flash their headlights back.

What does the tower's wind gauge read, in km/h? (0-200): 180
The tower groans in the gale. Anyone still on the hill should get down now.

Headlights flash from the bottom of the hill: your ride, asking if it is safe to come up.
Do you know tonight's answer code? (yes/no): yes
Tower backup battery remaining, as a percentage? (0-100): 80
You flash the code, and the truck starts up the hill.

==================================================
TOWER LOG: JJ
==================================================
Searchlight aimed: town
Cars in sight: 3
Wind reading: CRITICAL
Final status: PICKED UP
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

* the tower light comes on for `"yes"` and stays dark for anything else
* each of the three directions puts the right number of cars in sight
* each of the four wind statuses comes out of the right range, including exactly `80`
* you get picked up with the code and enough battery, stranded with the code alone, and left
  behind without the code no matter how full the battery is
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

* how the `if`/`else` decided whether the tower light lit or stayed dark
* why a reading of `180` reaches the branch you meant it to reach, and what a different ordering
  of that chain would do to it
* what the indentation of the ride home's inner `if` tells Python, and what changes if those
  two checks sit side by side instead

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
