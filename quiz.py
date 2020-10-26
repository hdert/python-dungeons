"""See quiz.__doc__."""

from random import randint as rand


def quiz(location, score):
    """D."""
    quiz_questions = [[
        """Write one of:
    Example
    None
    wasd""", """Fill in the *:
    Boom clap I'm in me mom's *"""
    ], [], []]
    quiz_answers = [[["Example", "None", "wasd"], ["car"]], [], []]
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 0:
        rand_choice = rand(0, len(current_questions) - 1)
        user_input = input(f"""
    {current_questions.pop(rand_choice)}
    : """)
        answers = current_answers.pop(rand_choice)
        if user_input in answers:
            input("""
    You got it right""")
            score[location - 1] += 1
        else:
            answers_text = ""  # initialize answers_text as a string
            for i in answers:
                answers_text += f"    {i},\n"
                # for each entry in answers, insert that answer with a leading
                # tab and trailing comma and newline
            answers_text = "".join(
                answers_text.rsplit(",\n", 1)
            )  # reverse version of string.replace(), replacing ",\n" with ""
            input(f"""
    You got it wrong.
    The answer was one of:
{answers_text}""")
    return (score[0], score[1], score[2])


if __name__ == "__main__":
    print(quiz(int(input()), [None, None, None]))
