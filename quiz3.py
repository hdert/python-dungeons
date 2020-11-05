"""See quiz.__doc__."""

from random import randint as rand
from out_of_range_error import out_of_range_error


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
    If there are 0 questions left in the current location, return the user
    scores.

    Args:
        location:
            The location of the user.
        score:
            The score of the user.
    Returns:
        The score of the user.
    """
    # Initialize lists of answers and questions
    quiz_questions = [
        [
            """What is the correct formula to find the sum of the internal
            angles of a polygon:""",
            """What is the correct formula to find the sum of the external
            angles of a polygon:"""
        ],
        [
            "What part of speech is the word jump:",
            """What language feature is this:
    Go clean your room right now this instance you naughty little
    devil child!""", """What type of poem is this:
    Go clean your room right
    now this instance you naughty
    little devil child!"""
        ],
        [
            "How many credits does a Level 1 student in 2020 need:",
            "How many credits will a Level 2 student need next year:"
        ]
    ]
    quiz_answers = [[["n - 2 * 180", "(n - 2)180", "n - 2 * 60", "360", 1],
                     ["n * 60", "n + 3 * 180", "(n + 3)180", "360", 3]],
                    [["Noun", "Verb", "Adjective", "Adverb", 1],
                     ["Hyperbole", "Rhetoric", "Imperative", "Sonnet", 2],
                     ["Sonnet", "Haiku", "Limerick", "Free verse", 1]],
                    [["80", "60", "72", "70", 3], ["80", "60", "72", "52", 1]]]
    # get the question answer, and score values to use based on the users
    # location
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 0:
        # Run while there are still questions left
        rand_choice = rand(0, len(current_questions) - 1)
        # pick a random question and answer
        answer = current_answers[rand_choice][
            4]  # get the integer that 'points' to the correct answer
        answer_text = current_answers[rand_choice][
            answer]  # feed this integer back in to get the text of the answer
        try:
            user_input = int(
                input(f"""
    {current_questions.pop(rand_choice)}
    1) {current_answers[rand_choice].pop(0)}
    2) {current_answers[rand_choice].pop(0)}
    3) {current_answers[rand_choice].pop(0)}
    4) {current_answers[rand_choice].pop(0)}
    [1-4]: """))  # give the user the randomly selected question and possible
            # answers
        except ValueError:  # if the user doesn't put in an interger, skip the
            # question and give them the error message
            out_of_range_error(4)
            user_input = None  # set user_input so the program doesn't break
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
