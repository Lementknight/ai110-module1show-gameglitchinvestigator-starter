# Refactored: all game logic moved here from app.py so it can be unit tested
# independently of the Streamlit UI

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    # Fix: Hard was returning (1, 50), which is easier than Normal (1, 100)
    # Changed to (1, 200) so Hard is actually harder
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str | None):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # Fix: hint messages were swapped — guessing too high said "Go HIGHER!"
    # and guessing too low said "Go LOWER!", which is backwards
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # Fix: "Too High" on even-numbered attempts previously gave +5 points,
    # rewarding a wrong guess. Both wrong outcomes now consistently deduct 5.
    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score