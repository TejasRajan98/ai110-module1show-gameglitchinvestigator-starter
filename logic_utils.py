def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: I spotted Hard (1-50) was easier than Normal; Claude explained why, moved this function here, and set 1-200 in agent mode
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Claude moved check_guess here from app.py in agent mode and fixed the str-vs-int comparison I asked it to look at
    # app.py passes the secret as a str on even attempts; compare numerically, not lexicographically
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: I flagged the swapped high/low hints; Claude corrected them and wrote pytest regression tests to confirm
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
