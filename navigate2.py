"""See navigate.__doc__."""
from out_of_range_error import out_of_range_error


def navigate(location=0):  # noqa: D205
    """Show the user the options for navigation and give them a prompt.
    Check that the user has selected a valid target and move their
    location to that target.

    Show the user the options for navigation by getting their location and
    finding possible exits through the relations list. Find the names of the
    rooms on the other side of the exits by consulting the rooms list. Give
    the user a prompt where they answer the room they want to go to as a
    number 1-4 corresponding to the number beside the room shown in the prompt.
    Make sure the room value is not 4 and return the users updated location.

    Args:
        location:
            Optional; The room the user is currently in, defaults to 0.

    Returns:
        The location of the user as an int.
    """
    room = [
        "Entrance", "Math Room", "English Room", "NCEA Headquaters",
        "Fancy Wall"
    ]

    relations = [[2, 4, 4, 4], [4, 4, 0, 4], [3, 0, 4, 4], [1, 4, 4, 0]]

    try:
        user_input = int(
            input(f"""
    Navigation:
    1) North: {room[relations[0][location]]};
    2) South: {room[relations[1][location]]};
    3) East: {room[relations[2][location]]};
    4) West: {room[relations[3][location]]};
    [1-4]: """))
    except ValueError:
        out_of_range_error(4)
        return navigate(location)
    if user_input in (1, 2, 3, 4):
        if relations[user_input - 1][location] == 4:
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        return relations[user_input - 1][location]
    out_of_range_error(4)
    return navigate(location)


if __name__ == "__main__":
    print(navigate(int(input())))
