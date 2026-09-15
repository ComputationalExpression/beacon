"""Beacon.

CMPSC 100: Computational Expression, Lab 2

Meet the Raspberry Pi Pico 2 W. Its built-in LED is a hilltop signal beacon,
and you are its keeper on the night a storm comes in. Every decision you make
tonight, the beacon answers with light.

Author: TODO
"""

from machine import Pin
import time


def main():
    led = Pin("LED", Pin.OUT)

    print("=" * 50)
    print("BEACON")
    print("=" * 50)

    # ===== Stage One: Light the Beacon =====

    # TODO 1: ask the keeper's name, save it to a variable called `name`

    # TODO 2: ask "yes" or "no" about lighting the beacon now that night has
    # fallen, save the answer to a variable called `beacon_on`

    # TODO 3: use if/else on beacon_on
    # if it is "yes": call led.on(), then print a message that uses `name` and
    # says the beacon glows
    # else: call led.off(), then print a message that uses `name` and says the
    # beacon stays dark

    # One pulse, so the beacon visibly answers whichever way it started
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
    print("Beacon signal confirmed.")

    # ===== Stage Two: Aim the Beacon =====

    print()
    print("The beacon turns on its mount.")

    # TODO 4: ask which way to aim it, "north", "south", or "east", and save
    # the answer to a variable called `direction`

    # TODO 5: use if/elif/else on `direction` to set a variable called
    # `villages` and print how many villages can see the light that way
    # "north": 3 villages
    # "south": 1 village
    # anything else: 2 villages

    # ===== Stage Three: The Wind Gauge =====

    print()

    # TODO 6: ask the wind gauge reading in km/h (0-200), save it to `wind`,
    # and convert it to an int

    # TODO 7: use an if/elif/elif/else chain to set a variable called
    # `wind_status` and print a matching message
    # 150 or more: "CRITICAL"
    # 80 or more: "HIGH"
    # 20 or more: "STEADY"
    # anything else: "CALM"
    # Order matters here. A reading of 180 is greater than every one of those
    # numbers, so whichever test you put first is the one that claims it
    # In the CRITICAL branch only, also flash the beacon three times, 0.1
    # seconds on and 0.1 seconds off each time: the storm warning

    # ===== Stage Four: The Answering Light =====

    print()
    print("A light flickers on the far ridge. The next keeper is waiting.")

    # TODO 8: ask whether the keeper has tonight's signal code ("yes"/"no"),
    # save it to `has_code`, then ask the beacon charge percentage (0-100),
    # save it to `charge`, and convert that one to an int

    # TODO 9: the signal needs BOTH the code and a charge of 40 or more, so
    # put one if inside another
    # outer if, has_code is "yes":
    #     inner if, charge is 40 or more: led.on(), set `outcome` to
    #     "RELAYED", print that the beacon blazes across the ridge
    #     inner else: led.off(), set `outcome` to "FADED", print that the
    #     beacon gutters out mid-signal
    # outer else: led.off(), set `outcome` to "SILENT", print that no signal
    # can go out without the code
    # The inner if belongs to the outer one, and its indentation is what says
    # so. Nothing else in Python marks where a block starts and ends

    print()
    print("=" * 50)

    # TODO 10: print the keeper's log, one line each, using f-strings
    # "KEEPER'S LOG: {name}", then a line of 50 "=" characters, then
    # "Aimed: {direction}", "Villages in sight: {villages}",
    # "Wind reading: {wind_status}", and "Final status: {outcome}"


if __name__ == "__main__":
    main()
