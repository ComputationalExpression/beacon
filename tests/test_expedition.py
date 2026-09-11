"""Automated checks for Lab 2: Cave Expedition."""

from unittest.mock import patch

from main import main


def run_with(name, beacon_on, steps, seconds, capsys):
    """Run main() once with a fixed sequence of answers and return what it printed."""
    answers = [name, beacon_on, str(steps), str(seconds)]
    # time.sleep is real here (mockro only mocks it under `import utime`), so
    # it is patched directly to keep tests instant regardless of loop length.
    with patch("builtins.input", side_effect=answers), patch("time.sleep", return_value=None):
        main()
    out, err = capsys.readouterr()
    assert err == ""
    return out


def test_program_runs_and_prints(capsys):
    out = run_with("JJ", "yes", 3, 3, capsys)
    # An untouched starter prints its provided framing text either way, so
    # checking for the adventurer's own name is what actually requires
    # Part One's TODOs to be done.
    assert "JJ" in out


def test_beacon_on(capsys):
    out = run_with("JJ", "yes", 3, 3, capsys)
    assert "JJ, your beacon glows." in out


def test_beacon_off(capsys):
    out = run_with("JJ", "no", 3, 3, capsys)
    assert "JJ, you leave your beacon dark." in out


def test_walking_steps(capsys):
    out = run_with("JJ", "yes", 3, 3, capsys)
    lines = out.split("\n")
    assert "  Step 1: the passage narrows around you." in lines
    assert "  Step 2: the passage narrows around you." in lines
    assert "  Step 3: the passage narrows around you." in lines
    assert "  Step 4: the passage narrows around you." not in lines


def test_steps_clamp_high(capsys):
    out = run_with("JJ", "yes", 15, 3, capsys)
    lines = out.split("\n")
    assert "  Step 10: the passage narrows around you." in lines
    assert "  Step 11: the passage narrows around you." not in lines


def test_steps_clamp_low(capsys):
    out = run_with("JJ", "yes", 0, 3, capsys)
    lines = out.split("\n")
    assert "  Step 1: the passage narrows around you." in lines
    assert "  Step 2: the passage narrows around you." not in lines


def test_countdown(capsys):
    out = run_with("JJ", "yes", 3, 3, capsys)
    lines = out.split("\n")
    assert "  3..." in lines
    assert "  2..." in lines
    assert "  1..." in lines
    assert "  0..." not in lines


def test_countdown_clamp_high(capsys):
    out = run_with("JJ", "yes", 3, 15, capsys)
    lines = out.split("\n")
    assert "  10..." in lines
    assert "  11..." not in lines


def test_countdown_clamp_low(capsys):
    out = run_with("JJ", "yes", 3, 1, capsys)
    lines = out.split("\n")
    assert "  3..." in lines
    assert "  2..." in lines
    assert "  1..." in lines


def test_star_pattern(capsys):
    out = run_with("JJ", "yes", 3, 3, capsys)
    lines = out.split("\n")
    assert "* " in lines
    assert "* * " in lines
    assert "* * * " in lines
    assert "* * * * " in lines
    assert "* * * * * " in lines
