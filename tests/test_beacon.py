"""Automated checks for Lab 2: Beacon on Pig Hill.

Every check reads the tower log at the end of the run, never the narrative
lines, so the story is the student's to word. Log values are matched loosely:
any amount of whitespace, any letter case, and the colon is optional, so
`print("Tree line:", tree_line)`, `print("Tree line: " + tree_line)`, and
`print(f"Tree line: {tree_line}")` all read the same.
"""

import re
from unittest.mock import patch

from main import main


def run_with(name, switch_on, wind, moved, heard, has_code, charge, capsys):
    """Run main() once with a fixed sequence of answers and return what it printed."""
    answers = [name, switch_on, str(wind), moved, heard, has_code, str(charge)]
    # time.sleep is real here (mockro only mocks it under `import utime`), so
    # it is patched directly to keep the tests instant.
    with patch("builtins.input", side_effect=answers), patch("time.sleep", return_value=None):
        main()
    out, err = capsys.readouterr()
    assert err == ""
    return out


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


# A run where every answer is the calm, safe one. Individual tests change
# exactly the answers they are about.
SAFE = dict(name="JJ", switch_on="yes", wind=50, moved="no", heard="no", has_code="yes", charge=80)


def run(capsys, **changes):
    answers = {**SAFE, **changes}
    return run_with(capsys=capsys, **answers)


def test_program_runs_and_log_names_you(capsys):
    # An untouched starter prints its provided framing text either way, so
    # checking for the user's own name in the log is what actually requires
    # Stage One and the tower log to be done.
    out = run(capsys)
    assert log_value(out, "TOWER LOG") == "JJ"


def test_tower_light_answers_yes_and_no(capsys):
    assert log_value(run(capsys, switch_on="yes"), "Tower light") == "LIT"
    assert log_value(run(capsys, switch_on="no"), "Tower light") == "DARK"


def test_wind_strongest_reading_is_critical(capsys):
    # 180 satisfies every threshold in the chain, so only a chain that tests
    # the strongest range first can report it correctly.
    assert log_value(run(capsys, wind=180), "Wind reading") == "CRITICAL"


def test_wind_each_threshold_is_inclusive(capsys):
    # Exactly the threshold belongs to the range it starts: "80 or more" is HIGH.
    assert log_value(run(capsys, wind=150), "Wind reading") == "CRITICAL"
    assert log_value(run(capsys, wind=80), "Wind reading") == "HIGH"
    assert log_value(run(capsys, wind=20), "Wind reading") == "STEADY"
    assert log_value(run(capsys, wind=5), "Wind reading") == "CALM"


def test_tree_line_one_sign_alone_is_enough(capsys):
    # Either sign on its own has to be enough. A condition written with `and`
    # instead of `or` passes only when both are present, and fails both of these.
    assert log_value(run(capsys, moved="yes", heard="no"), "Tree line") == "NOT ALONE"
    assert log_value(run(capsys, moved="no", heard="yes"), "Tree line") == "NOT ALONE"


def test_tree_line_clear_without_either_sign(capsys):
    assert log_value(run(capsys, moved="no", heard="no"), "Tree line") == "CLEAR"
    assert log_value(run(capsys, moved="yes", heard="yes"), "Tree line") == "NOT ALONE"


def test_ride_charge_decides_once_the_code_is_known(capsys):
    assert log_value(run(capsys, has_code="yes", charge=80), "Final status") == "PICKED UP"
    assert log_value(run(capsys, has_code="yes", charge=10), "Final status") == "STRANDED"


def test_ride_full_charge_never_answers_without_the_code(capsys):
    # A full charge must not answer the truck on its own. Two separate ifs
    # sitting side by side would let it; the charge check has to be nested
    # inside the code check, so that it is never reached without the code.
    out = run(capsys, has_code="no", charge=100)
    assert log_value(out, "Final status") == "LEFT BEHIND"
    assert "PICKED UP" not in out.upper()
