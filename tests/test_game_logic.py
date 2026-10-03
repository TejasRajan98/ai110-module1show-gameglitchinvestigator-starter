from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the fixed bugs ---

def test_too_high_guess_tells_player_to_go_lower():
    # Bug: hints were swapped, so a guess above the secret said "Go HIGHER!"
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_guess_tells_player_to_go_higher():
    # Bug: hints were swapped, so a guess below the secret said "Go LOWER!"
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_string_secret_is_compared_numerically():
    # Bug: app.py passes the secret as a str on even attempts, and the old
    # fallback compared strings alphabetically ("9" > "50").
    assert check_guess(9, "50")[0] == "Too Low"
    assert check_guess(100, "50")[0] == "Too High"
    assert check_guess(50, "50")[0] == "Win"

def test_hard_range_is_wider_than_normal():
    # Bug: Hard was 1-50, narrower than Normal's 1-100, so it was easier.
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high > easy_high
    assert easy_low == normal_low == hard_low == 1
