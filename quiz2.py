"""See quiz.__doc__."""

from random import randint as rand


def quiz(location, score):
    """D."""
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
            answers_text = ",\n    ".join(answers)
            input(f"""
    You got it wrong.
    The answer was one of:
    {answers_text}""")
    return (score[0], score[1], score[2])


if __name__ == "__main__":
    print(quiz(int(input()), [None, None, None]))
