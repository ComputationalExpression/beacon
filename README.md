# Lab 2: Cave Expedition

|Item |       |
|:----|:------|
|Released |Week 4, Friday lecture |
|Due |See the [course schedule](https://computationalexpression.com/schedule/) |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

This lab spans two weeks. Part One turns your Raspberry Pi Pico 2 W's built-in LED into a
beacon using what you already know: conditionals. Part Two sends that beacon through a cave
expedition told entirely in `for` loops, once next week's lecture covers them.

## Course learning outcomes

This lab addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this lab you should be able to:

* control a physical device's output with `machine.Pin` and `time.sleep`
* choose the correct branch of an `if`/`else` based on a condition
* write a `for` loop over `range()`, including a loop that counts backward
* nest one `for` loop inside another to build a two-dimensional pattern
* clamp a user-provided number into a valid range with `if` statements

## Meet the Pico 2 W

Your Pico 2 W is a microcontroller, not a small computer: your program runs directly against
the hardware, with nothing in between. `Pin("LED", Pin.OUT)` gives you control of the board's
built-in LED; `led.on()` and `led.off()` send it 3.3V and 0V. See Wednesday's slides for the
fuller explanation of what is happening electrically.

**Setup, one time only:**

1. Install the **MicroPico** extension by **paulober** in VS Code, if you have not already
   (from the [setup guide](https://computationalexpression.com/setup/))
2. Plug in your Pico 2 W over USB
3. Press `Ctrl/Cmd+Shift+P`, then run **MicroPico: Initialize MicroPico**
4. Confirm you see **MicroPico** in the bottom status bar

If it will not connect, ask an instructor or TL. Do not troubleshoot hardware alone the night
before it is due.

## Part One: Beacon Check

Released Friday, due whenever the lab as a whole is due. Uses only `input()` and `if`/`else`,
nothing from next week.

Ask the adventurer's name and whether to turn the beacon on, then use `if`/`else` on the
answer to call `led.on()` or `led.off()` and print the matching message. The rest of the file
(the confirmation pulse, and everything under `PART TWO`) is already provided.

## Part Two: Into the Cave

Come back to this part after Monday's loop lecture. It uses `for` loops throughout, and
nothing here requires anything beyond what Monday covers.

* **Walking Steps**: a `for` loop over `range(1, steps + 1)` pulses the beacon once per step
* **Countdown Chamber**: a `for` loop over `range(seconds, 0, -1)` counts backward, pulsing
  faster each time
* **Star Pattern**: a loop inside a loop builds a five-row triangle, one `"* "` at a time

Both `steps` and `seconds` are numbers the user types in, clamped into a valid range with `if`
statements before the loop that uses them runs.

### Expected output

```text
==================================================
CAVE EXPEDITION: BEACON CHECK
==================================================
Adventurer, what is your name? JJ
Turn on your beacon before you enter the cave? (yes/no): yes
JJ, your beacon glows. You step toward the cave entrance.
Beacon signal confirmed.

==================================================
PART TWO: INTO THE CAVE
==================================================
How many steps into the darkness? (1-10): 3
You start walking, beacon pulsing with every step...
  Step 1: the passage narrows around you.
  Step 2: the passage narrows around you.
  Step 3: the passage narrows around you.
You reach a wide chamber and catch your breath.
An old mechanism starts counting down. Seconds? (3-10): 3
The chamber counts down with you:
  3...
  2...
  1...
The mechanism falls silent. A passage opens ahead.
A wall of ancient stars waits to be traced:
* 
* * 
* * * 
* * * * 
* * * * * 
The stars align, and the final passage reveals itself.

==================================================
EXPEDITION COMPLETE
==================================================
```

## Getting started

Open `src/main.py` and work through the `TODO` markers in order, Part One before Part Two. Run
it on your Pico as you go, using MicroPico's **Run current file** command, or from the terminal
against a plain Python interpreter for the parts that do not depend on real hardware timing:

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
| Programming | 3.0 | The 10 code checks below. Your score is the fraction passed, times 3.0 |
| Code quality and style | 1.0 | Descriptive names (0.3), clear organization (0.3), useful comments (0.4) |
| Summary writing | 0.5 | A complete, thoughtful `docs/summary.md` |
| **Total** | **4.5** | |

### Programming, 3.0 points

Run the checks yourself, as many times as you like, before you submit:

```text
uv run gatorgrade --config gatorgrade.yml
```

Ten of the checks are about your code:

* the beacon turns on for `"yes"` and off for anything else
* the walking-steps loop prints the right number of steps, clamped between 1 and 10
* the countdown counts down correctly, clamped between 3 and 10
* the star pattern forms a five-row triangle
* no `TODO` markers remain in `src/main.py`, and it uses `for` loops (never `while`)

Partial credit is proportional: passing 8 of 10 checks earns `(8 ÷ 10) × 3.0 = 2.4` points.

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

* how the `if`/`else` decided whether the beacon turned on or off
* what `range(1, steps + 1)` and `range(seconds, 0, -1)` each produce, and why
* how the inner loop builds each row of the star pattern, one `"* "` at a time

**Your review must be completed during the lab session on the day this lab is due.** If you
cannot attend that lab and complete your review then, make arrangements to complete it
beforehand at office hours:

* **Technical Leaders**, listed on the calendar at
  [cis.allegheny.edu/community/news](https://www.cis.allegheny.edu/community/news/)
* **Dr. Jumadinova**, [book a time](https://janyljumadinova.com/schedule). Drop-ins are welcome
  during posted hours, but students who booked are seen first

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded. If you need more time, apply a late token with
[this form](https://forms.gle/3nGbpaNrG96DpLLdA).

**In the terminal:**

```text
git add src/main.py docs/summary.md
git commit -m "Complete the cave expedition"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it (this is `git add`)
2. Type a message in the box at the top, then click the checkmark (this is `git commit`)
3. Click **Sync Changes** (or the &uarr; arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.
