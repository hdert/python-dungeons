"""See quiz_check.__doc__."""


def quiz_check(location, score):
    """Check if there is an unplayed quiz in the users current room."""
    if (
        (location == 1 and score[0] is not None)
            or (location == 2 and score[1] is not None)
            or (location == 3 and score[2] is not None)
    ):  # checks if the room has a score ∴ checking if the room has been played
        return False
    return True


if __name__ == "__main__":
    for x in range(4):  # The player location to iterate through
        for y in range(
                2):  # Toggles between having a score and not having a score
            print(
                quiz_check(x, [
                    None if y == 0 else 1, None if y == 0 else 1,
                    None if y == 0 else 1
                ]))
