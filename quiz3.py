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
    2. Set the answer and answer text to answer and answer_text
    2. Give the user a prompt to type their answer, therein deleting the
    question from the question list. Convert this input to an integer
    3. Check that the user input matches answer
        3.1 If the answer was right, iterate the user score and display
        'You got it right'.
        3.2 If not display the correct answer using answer_text.
    If there are 0 questions return the user scores.
    """
    # Initialize lists of answers and questions
    quiz_questions = [[
        """The answer is Example:""", """Finish the lyrics:
    Boom clap I'm in me mom's *"""
    ], [], []]
    quiz_answers = [[["Example", "None", "wasd", "Not Example", 0],
                     ["car", "room", "house", "town", 0]], [], []]
    # get the question answer, and score values to use based on the users
    # location
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 0:
        # Run while there are still questions left
        rand_choice = rand(0, len(current_questions) - 1)
        # pick a random question and answer
        answer = current_answers[rand_choice][4]
        answer_text = current_answers[rand_choice][current_answers[rand_choice]
                                                   [4]]
        try:
            user_input = int(
                input(f"""
    {current_questions.pop(rand_choice)}
    1) {current_answers[rand_choice].pop(0)}
    2) {current_answers[rand_choice].pop(0)}
    3) {current_answers[rand_choice].pop(0)}
    4) {current_answers[rand_choice].pop(0)}
    [1-4]: """))  # give the user the randomly selected question,
        except ValueError:
            input("""
    When prompted, enter one of the numbers 1, 2, 3, 4.
    Each number corresponds to an action printed on screen""")
            user_input = None
        # delete the question from the master list, and take user input
        current_answers.pop(rand_choice)
        # get the answers to the randomly selected question
        if user_input in (1, 2, 3, 4):  # check if the users input is valid
            if user_input - 1 == answer:
                input("""
    You got it right""")
                score[location - 1] += 1
            else:
                input(f"""
    You got it wrong.
    The answer was:
    {answer_text}""")
    return score


if __name__ == "__main__":
    print(quiz(int(input()), [None, None, None]))
