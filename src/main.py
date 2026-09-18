"""Beacon on Pig Hill.

CMPSC 100: Computational Expression, Lab 2

Meet the Raspberry Pi Pico 2 W. Its built-in LED is the red warning light on
the radio tower above Meadville, on the hill everyone calls Pig Hill, and
tonight you are the one keeping it lit. Every decision you make up there, the
light answers.

Author: TODO
"""

from machine import Pin
import time


def main():
    led = Pin("LED", Pin.OUT)

    print("=" * 50)
    print("BEACON ON PIG HILL")
    print("=" * 50)

    # ===== Stage One: Light the Tower =====

    # TODO 1: ask the user's name, save it to a variable called `name`

    # TODO 2: ask "yes" or "no" about switching on the tower light now that
    # the sun is down, save the answer to a variable called `switch_on`

    # TODO 3: use if/else on `switch_on`
    # if it is "yes": call led.on(), set a variable called `light` to "LIT",
    # and print a message that uses `name`
    # else: call led.off(), set `light` to "DARK", and print a message that
    # uses `name`

    # ===== Stage Two: The Wind Gauge =====

    print()

    # TODO 4: ask the tower's wind gauge reading in km/h (0-200), save it to
    # `wind`, and convert it to an int

    # TODO 5: use an if/elif/elif/else chain to set a variable called
    # `wind_status` and print a matching message
    # 150 or more: "CRITICAL"
    # 80 or more: "HIGH"
    # 20 or more: "STEADY"
    # anything else: "CALM"
    # Order matters here. A reading of 180 is greater than every one of those
    # numbers, so whichever test you put first is the one that claims it
    # In the CRITICAL branch only, also flash the light three times, 0.1
    # seconds on and 0.1 seconds off each time: the warning every driver in
    # Meadville knows

    # ===== Stage Three: The Tree Line =====

    print()
    print("Two points of light blink on at the tree line, low to the ground and too far apart to be a deer.")

    # TODO 6: ask two "yes"/"no" questions, in this order: do the points of
    # light move when your light hits them (save it to `moved`), then do you
    # hear anything from the trees (save it to `heard`)

    # TODO 7: either sign on its own means you are not alone up here, so
    # write ONE if whose condition joins the two answers with `or`
    # if either is "yes": call led.off(), set a variable called `tree_line`
    # to "NOT ALONE", and print what you do
    # else: set `tree_line` to "CLEAR" and print what you tell yourself

    # ===== Stage Four: The Ride Home =====

    print()
    print("Headlights flash from the bottom of the hill: your ride, asking if it is safe to come up.")

    # TODO 8: ask whether the user knows tonight's answer code ("yes"/"no"),
    # save it to `has_code`, then ask the tower backup battery percentage
    # (0-100), save it to `charge`, and convert that one to an int

    # TODO 9: the answer needs BOTH the code and a charge of 40 or more, and
    # the two ways it can go wrong need different messages, so put one if
    # inside another rather than joining them with `and`
    # outer if, has_code is "yes":
    #     inner if, charge is 40 or more: led.on(), set `outcome` to
    #     "PICKED UP", print that the truck starts up the hill
    #     inner else: led.off(), set `outcome` to "STRANDED", print that the
    #     battery dies halfway through the code and the truck turns around
    # outer else: led.off(), set `outcome` to "LEFT BEHIND", print that the
    # truck waits, then leaves without you
    # The inner if belongs to the outer one, and its indentation is what says
    # so. Nothing else in Python marks where a block starts and ends

    print()
    print("=" * 50)

    # TODO 10: print the tower log, one line each, in this order:
    # "TOWER LOG: {name}", then a line of 50 "=" characters, then
    # "Tower light: {light}", "Wind reading: {wind_status}",
    # "Tree line: {tree_line}", and "Final status: {outcome}"
    # Print each value any way you like: commas, + with str(), or an f-string


if __name__ == "__main__":
    main()
