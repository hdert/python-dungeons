"""See quiz_check.__doc__."""


def quiz_check(location, score_one, score_two, score_three):
    """Check if there is an unplayed quiz in the users current room."""
    if ((location == 1 and score_one is not None)
            or (location == 2 and score_two is not None)
            or (location == 3 and score_three is not None)):
        return True
    return False


if __name__ == "__main__":
    print(
        quiz_check(int(input("""
    Location: """)), None, int(input("""
    Score two: """)), int(input("""
    Score three: """))))
