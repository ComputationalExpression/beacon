"""Cave Expedition.

CMPSC 100: Computational Expression, Lab 2

Meet the Raspberry Pi Pico 2 W and control its built-in LED, then use that
LED as a beacon through a short cave expedition told in for loops.

Author: TODO
"""

from machine import Pin
import time


def main():
    led = Pin("LED", Pin.OUT)

    print("=" * 50)
    print("CAVE EXPEDITION: BEACON CHECK")
    print("=" * 50)

    # ===== Part One: Beacon Check =====
    # Everything in this part uses only what you already know: input(), if/else.

    # TODO 1: ask the adventurer's name, save it to a variable called `name`

    # TODO 2: ask "yes" or "no" for whether to turn on the beacon before
    # entering the cave, save it to a variable called `beacon_on`

    # TODO 3: use if/else on beacon_on
    # if "yes": call led.on(), then print a message using `name` that the
    # beacon glows
    # else: call led.off(), then print a message using `name` that the
    # beacon stays dark

    # One pulse, so the beacon visibly responds whichever way it started
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
    print("Beacon signal confirmed.")

    print()
    print("=" * 50)
    print("PART TWO: INTO THE CAVE")
    print("=" * 50)

    # ===== Part Two: Into the Cave =====
    # This part uses for loops. Come back to it after Monday's loop lecture
    # -- Part One above is everything you need for this Friday.

    # TODO 4: ask how many steps into the darkness (1-10), save to `steps`,
    # convert it to an int
    # TODO 5: use if statements to clamp steps: if greater than 10, set it
    # to 10; if less than 1, set it to 1

    print("You start walking, beacon pulsing with every step...")
    # TODO 6: use a for loop with range(1, steps + 1) so the loop variable
    # counts each step starting at 1
    # For each step:
    #   - print "  Step {step}: the passage narrows around you."
    #   - turn the beacon on, sleep 0.2 seconds, turn it off, sleep 0.2 seconds
    print("You reach a wide chamber and catch your breath.")

    # TODO 7: ask how many seconds the countdown should last (3-10), save to
    # `seconds`, convert it to an int
    # TODO 8: use if statements to clamp seconds: if greater than 10, set it
    # to 10; if less than 3, set it to 3

    print("The chamber counts down with you:")
    # TODO 9: use a for loop that counts DOWN from seconds to 1
    # range() can step backwards if you give it a negative step: figure out
    # what starting value, ending value, and step count down to 1
    # For each number:
    #   - print "  {remaining}..."
    #   - turn the beacon on, sleep 0.15 seconds, turn it off, sleep 0.15
    #     seconds
    print("The mechanism falls silent. A passage opens ahead.")

    print("A wall of ancient stars waits to be traced:")
    pattern_size = 5
    # TODO 10: build a triangle of stars, five rows tall
    # Outer loop: for row in range(1, pattern_size + 1)
    # For each row:
    #   - build a string `line` that starts empty, then add "* " to it
    #     `row` times using an inner for loop
    #   - print(line) once the inner loop finishes
    print("The stars align, and the final passage reveals itself.")

    print()
    print("=" * 50)
    print("EXPEDITION COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()
