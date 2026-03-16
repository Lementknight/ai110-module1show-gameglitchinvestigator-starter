from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- get_range_for_difficulty ---


def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 200)


def test_range_unknown_defaults_to_normal():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# --- parse_guess ---


def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_not_a_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_float_truncates():
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3
    assert err is None


# --- check_guess ---


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- update_score ---


def test_update_score_win_early():
    # Attempt 1: 100 - 10*(1+1) = 80 points
    assert update_score(0, "Win", 1) == 80


def test_update_score_win_late():
    # Attempt 8: 100 - 10*(8+1) = 10 points
    assert update_score(0, "Win", 8) == 10


def test_update_score_win_clamps_to_minimum():
    # Attempt 10: 100 - 10*(10+1) = -10 → clamped to 10
    assert update_score(0, "Win", 10) == 10


def test_update_score_too_high_deducts():
    assert update_score(100, "Too High", 1) == 95


def test_update_score_too_low_deducts():
    assert update_score(100, "Too Low", 1) == 95


def test_update_score_unknown_outcome_unchanged():
    assert update_score(100, "SomethingElse", 1) == 100
