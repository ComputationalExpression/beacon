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
    # the sun is down, save the answer to a variable called `beacon_on`

    # TODO 3: use if/else on beacon_on
    # if it is "yes": call led.on(), then print a message that uses `name` and
    # says the tower light glows
    # else: call led.off(), then print a message that uses `name` and says the
    # tower stays dark

    # One pulse, so the light visibly answers whichever way it started
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
    print("Beacon signal confirmed.")

    # ===== Stage Two: Aim the Searchlight =====

    print()
    print("Headlights are moving on the roads below the tower.")

    # TODO 4: ask which way to aim the searchlight, "town", "road", or
    # "woods", and save the answer to a variable called `direction`

    # TODO 5: use if/elif/else on `direction` to set a variable called `cars`
    # and print what the searchlight finds that way
    # "town": 3 cars
    # "road": 1 car
    # anything else: 2 cars

    # ===== Stage Three: The Wind Gauge =====

    print()

    # TODO 6: ask the tower's wind gauge reading in km/h (0-200), save it to
    # `wind`, and convert it to an int

    # TODO 7: use an if/elif/elif/else chain to set a variable called
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

    # ===== Stage Four: The Ride Home =====

    print()
    print("Headlights flash from the bottom of the hill: your ride, asking if it is safe to come up.")

    # TODO 8: ask whether the user knows tonight's answer code ("yes"/"no"),
    # save it to `has_code`, then ask the tower backup battery percentage
    # (0-100), save it to `charge`, and convert that one to an int

    # TODO 9: the answer needs BOTH the code and a charge of 40 or more, so
    # put one if inside another
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

    # TODO 10: print the tower log, one line each, using f-strings
    # "TOWER LOG: {name}", then a line of 50 "=" characters, then
    # "Searchlight aimed: {direction}", "Cars in sight: {cars}",
    # "Wind reading: {wind_status}", and "Final status: {outcome}"


if __name__ == "__main__":
    main()
