"""See quiz_check.__doc__."""


def quiz_check(location, score):
    """Check if there is an unplayed quiz in the users current room.

    Args:
        location:
            The location of the user.
        score:
            The score of the user.
    Returns:
        A boolean value, True if there is a quiz, False if there is not.
    """
    if ((location == 1 and score[0] is not None)
            or (location == 2 and score[1] is not None)
            or (location == 3
                and score[2] is not None)):  # check if the room has a score
        # ∴ check if the room has been played
        return False
    if (
            location == 0
    ):  # check if the room is the entrace room ∴ the room doesn't have a quiz
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
