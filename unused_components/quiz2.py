"""See quiz.__doc__."""

from random import randint as rand


def quiz(location, score):
    """Give the user an interactive quiz based on their location.

    Use the user's location find the correct set of quiz_questions and
    quiz_answers to use. Assign these questions and answers to
    current_questions and current_answers. Use the user's location to find and
    set the appropriate score to 0. While there are more than 0 questions do
    the following:
    1. Pick a random question in the range of questions left.
    2. Give the user a prompt to type their answer, therein deleting the
    question from the question list.
    3. Check against the answers list, therein deleting the answer from the
    answers list.
        3.1 If the answer was right, iterate the user score.
        3.2 If not display the correct answers.
    If there are 0 questions return the user scores.
    """
    # Initialize lists of answers and questions
    quiz_questions = [[
        """Write one of:
    Example
    None
    wasd""", """Fill in the *:
    Boom clap I'm in me mom's *"""
    ], [], []]
    quiz_answers = [[["Example", "None", "wasd"], ["car"]], [], []]
    # get the question answer, and score values to use based on the users
    # location
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 0:
        # Run while there are still questions left
        rand_choice = rand(0, len(current_questions) - 1)
        # pick a random question and answer
        user_input = input(f"""
    {current_questions.pop(rand_choice)}
    : """)  # give the user the randomly selected question,
        # delete the question from the master list, and take user input
        answers = current_answers.pop(rand_choice)
        # get the answers to the randomly selected question
        if user_input in answers:  # check if the users input is
            input("""
    You got it right""")
            score[location - 1] += 1
        else:
            input("""
    You got it wrong.
    The answer was one of:
    {}""".format(",\n    ".join(answers)))
    return score


if __name__ == "__main__":
    print(quiz(int(input()), [None, None, None]))
