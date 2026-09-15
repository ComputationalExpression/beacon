"""Automated checks for Lab 2: Beacon."""

from unittest.mock import patch

from main import main


def run_with(name, beacon_on, direction, wind, has_code, charge, capsys):
    """Run main() once with a fixed sequence of answers and return what it printed."""
    answers = [name, beacon_on, direction, str(wind), has_code, str(charge)]
    # time.sleep is real here (mockro only mocks it under `import utime`), so
    # it is patched directly to keep the tests instant.
    with patch("builtins.input", side_effect=answers), patch("time.sleep", return_value=None):
        main()
    out, err = capsys.readouterr()
    assert err == ""
    return out


def test_program_runs_and_prints(capsys):
    out = run_with("JJ", "yes", "north", 50, "yes", 80, capsys)
    # An untouched starter prints its provided framing text either way, so
    # checking for the keeper's own name is what actually requires Stage
    # One's TODOs to be done.
    assert "JJ" in out


def test_beacon_on(capsys):
    out = run_with("JJ", "yes", "north", 50, "yes", 80, capsys)
    assert "glows" in out


def test_beacon_off(capsys):
    out = run_with("JJ", "no", "north", 50, "yes", 80, capsys)
    assert "dark" in out


def test_aim_north(capsys):
    out = run_with("JJ", "yes", "north", 50, "yes", 80, capsys)
    assert "Aimed: north" in out
    assert "Villages in sight: 3" in out


def test_aim_south(capsys):
    out = run_with("JJ", "yes", "south", 50, "yes", 80, capsys)
    assert "Aimed: south" in out
    assert "Villages in sight: 1" in out


def test_aim_east(capsys):
    out = run_with("JJ", "yes", "east", 50, "yes", 80, capsys)
    assert "Aimed: east" in out
    assert "Villages in sight: 2" in out


def test_wind_critical(capsys):
    out = run_with("JJ", "yes", "north", 180, "yes", 80, capsys)
    assert "Wind reading: CRITICAL" in out


def test_wind_high(capsys):
    out = run_with("JJ", "yes", "north", 100, "yes", 80, capsys)
    assert "Wind reading: HIGH" in out


def test_wind_steady(capsys):
    out = run_with("JJ", "yes", "north", 45, "yes", 80, capsys)
    assert "Wind reading: STEADY" in out


def test_wind_calm(capsys):
    out = run_with("JJ", "yes", "north", 5, "yes", 80, capsys)
    assert "Wind reading: CALM" in out


def test_wind_boundary_is_inclusive(capsys):
    # Exactly 80 belongs to HIGH, not STEADY: the test is "80 or more"
    out = run_with("JJ", "yes", "north", 80, "yes", 80, capsys)
    assert "Wind reading: HIGH" in out


def test_signal_relayed_with_code_and_charge(capsys):
    out = run_with("JJ", "yes", "north", 50, "yes", 80, capsys)
    assert "Final status: RELAYED" in out


def test_signal_faded_when_charge_is_low(capsys):
    out = run_with("JJ", "yes", "north", 50, "yes", 10, capsys)
    assert "Final status: FADED" in out


def test_signal_silent_without_code(capsys):
    # A full charge must not send the signal on its own. Two separate ifs
    # sitting side by side would let it; the charge check has to be nested
    # inside the code check, so that it is never reached without the code.
    out = run_with("JJ", "yes", "north", 50, "no", 100, capsys)
    assert "Final status: SILENT" in out
    assert "Final status: RELAYED" not in out
