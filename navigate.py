"""See navigate.__doc__."""

room = [
    "Crypt Entrance", "Math Room", "English Room", "NCEA Headquaters",
    "Fancy Wall"
]

N = [2, 4, 4, 4]

S = [4, 4, 0, 4]

E = [3, 0, 4, 4]

W = [1, 4, 4, 0]

desc = [
    "A dull enclosed space with three doors",
    "A dull enclosed space with one door",
    "A dull enclosed space with one door",
    "A dull enclosed space with one door"
]


def navigate(location=0):  # noqa: D205
    """Show the user the options for navigation and give them a prompt.
    Check that the user has selected a valid target and move their
    location to that target.

    Show the user the options for navigation by getting their location and
    finding possible exits through the NSEW lists. Find the names of the rooms
    on the other side of the exits by consulting the room list and the
    description list. Give the user a prompt where they answer the room they
    want to go to as a number 1-4 corresponding to the number beside the room
    shown in the prompt. Make sure the room is not 4 and return the users
    updated location.

    Args:
        location:
            Optional; The room the user is currently in, defaults to 0.

    Returns:
        The location of the user as an int.
    """
    user_input = input(f"""
    Navigation:
    1) North: {room[N[location]]};
    2) South: {room[S[location]]};
    3) East: {room[E[location]]};
    4) West: {room[W[location]]};
    [1-4]: """)
    if user_input == '1':
        if N[location] == 4:
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        return N[location]
    elif user_input == '2':
        if S[location] == 4:
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        return S[location]
    elif user_input == '3':
        if E[location] == 4:
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        return E[location]
    elif user_input == '4':
        if W[location] == 4:
            input("""
    That wall sure looks like a hidden entrance. You try and activate it,
    it doesn't react.""")
            return navigate(location)
        return W[location]
    else:
        input("""
    When prompted, enter one of the numbers 1, 2, 3, 4.
    Each number corresponds to an action printed on screen""")
        return navigate(location)


if __name__ == "__main__":
    print(navigate())
