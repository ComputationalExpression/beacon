"""Automated checks for Lab 2: Beacon on Pig Hill.

Every check reads the tower log at the end of the run, never the narrative
lines, so the story is the student's to word. Log values are matched loosely:
any amount of whitespace, any letter case, and the colon is optional, so
`print("Tree line:", tree_line)`, `print("Tree line: " + tree_line)`, and
`print(f"Tree line: {tree_line}")` all read the same.

When a check fails, the assertion message says which log line came out wrong,
what it said, what was expected, and the answers that were typed. gatorgrade
does not show that message itself; it prints the pytest command to run.
"""

import re
from unittest.mock import patch

from main import main

# The order the starter asks its questions. The checks type answers in this
# order, so a program that asks them in a different order reads the wrong
# answer for the wrong question.
QUESTIONS = ["name", "switch_on", "wind", "moved", "heard", "has_code", "charge"]

# A run where every answer is the calm, safe one. Individual checks change
# exactly the answers they are about.
SAFE = dict(name="JJ", switch_on="yes", wind=50, moved="no", heard="no", has_code="yes", charge=80)


def run(capsys, **changes):
    """Run main() once with the SAFE answers plus `changes`, and return what it printed."""
    answers = {**SAFE, **changes}
    typed = [str(answers[q]) for q in QUESTIONS]
    # time.sleep is real here (mockro only mocks it under `import utime`), so
    # it is patched directly to keep the checks instant.
    with patch("builtins.input", side_effect=typed), patch("time.sleep", return_value=None):
        main()
    out, err = capsys.readouterr()
    assert err == "", "the program wrote to the error stream:\n" + err
    return out, answers


def log_value(out, label):
    """Return the value printed after `label` in the tower log, normalized.

    Only the part of the output from `TOWER LOG` onward is searched, so a
    narrative line that happens to mention the tower light cannot be mistaken
    for the log entry. Whitespace is collapsed, case is folded to upper, a
    trailing period is dropped, and the colon after the label is optional.
    Returns None when the log, or the label, was never printed.
    """
    start = out.upper().find("TOWER LOG")
    if start < 0:
        return None
    match = re.search(rf"{label}\s*:?\s*([^\n]*)", out[start:], re.IGNORECASE)
    if match is None:
        return None
    return " ".join(match.group(1).split()).upper().rstrip(".! ")


def expect(capsys, label, want, **changes):
    """Run once and check that the tower log line `label` says `want`."""
    out, answers = run(capsys, **changes)
    typed = ", ".join(f"{q}={answers[q]}" for q in QUESTIONS)
    if "TOWER LOG" not in out.upper():
        raise AssertionError(f'no "TOWER LOG" line was printed (answers typed: {typed})')
    got = log_value(out, label)
    if got is None:
        raise AssertionError(f'no "{label}" line was printed after TOWER LOG (answers typed: {typed})')
    assert got == want, f'the "{label}" line said {got}, expected {want} (answers typed: {typed})'
    return out


def test_program_runs_and_log_names_you(capsys):
    # An untouched starter prints its provided framing text either way, so
    # checking for the user's own name in the log is what actually requires
    # Stage One and the tower log to be done.
    expect(capsys, "TOWER LOG", "JJ")


def test_tower_light_answers_yes_and_no(capsys):
    expect(capsys, "Tower light", "LIT", switch_on="yes")
    expect(capsys, "Tower light", "DARK", switch_on="no")


def test_wind_strongest_reading_is_critical(capsys):
    # 180 satisfies every threshold in the chain, so only a chain that tests
    # the strongest range first can report it correctly.
    expect(capsys, "Wind reading", "CRITICAL", wind=180)


def test_wind_each_threshold_is_inclusive(capsys):
    # Exactly the threshold belongs to the range it starts: "80 or more" is HIGH.
    expect(capsys, "Wind reading", "CRITICAL", wind=150)
    expect(capsys, "Wind reading", "HIGH", wind=80)
    expect(capsys, "Wind reading", "STEADY", wind=20)
    expect(capsys, "Wind reading", "CALM", wind=5)


def test_tree_line_one_sign_alone_is_enough(capsys):
    # Either sign on its own has to be enough. A condition written with `and`
    # instead of `or` holds only when both are present, and fails both of these.
    expect(capsys, "Tree line", "NOT ALONE", moved="yes", heard="no")
    expect(capsys, "Tree line", "NOT ALONE", moved="no", heard="yes")


def test_tree_line_clear_without_either_sign(capsys):
    expect(capsys, "Tree line", "CLEAR", moved="no", heard="no")
    expect(capsys, "Tree line", "NOT ALONE", moved="yes", heard="yes")


def test_ride_charge_decides_once_the_code_is_known(capsys):
    expect(capsys, "Final status", "PICKED UP", has_code="yes", charge=80)
    expect(capsys, "Final status", "STRANDED", has_code="yes", charge=10)


def test_ride_full_charge_never_answers_without_the_code(capsys):
    # A full charge must not answer the truck on its own. Two separate ifs
    # sitting side by side would let it: the charge check has to be nested
    # inside the code check, or joined to it with `and`, so that the battery
    # is never consulted without the code.
    out = expect(capsys, "Final status", "LEFT BEHIND", has_code="no", charge=100)
    assert "PICKED UP" not in out.upper(), "PICKED UP was printed even though the code was not known"
