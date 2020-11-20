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
    angles of a polygon:""",
            """Substitute u = 3 and t = 5 into the following equation:
    d = ut + 3t²""", "Solve the equation 10x² - 27x - 9 = 0",
            """What is (8x - 1)/(4) + (3x-5)/(3) as a simplified single
    fraction""", "What is (3x² + 9x)/(x² - 9) as a simplified single fraction",
            """fk² - 9c² = 4d² + 16gk², Give the equation for k in terms of c,
    d, f, and g.""", "What is 3 * 5", "5³",
            "What does SOH in SOH CAH TOA stand for",
            "What does CAH in SOH CAH TOA stand for",
            "What does TOA in SOH CAH TOA stand for",
            "Angles on a line add to", "Angles on a point add to",
            "Vertically opposite angles", "Angles in a Triangle",
            "Angles in a Square", "An exterior angle of a triangle equals",
            "In an isosceles triangle", "Co-Interior angles on parallel lines"
        ],
        [
            "What part of speech is the word jump:",
            """What language feature is this:
    Go clean your room right now this instance you naughty little
    devil child!""", """What type of poem is this:
    Go clean your room right
    now this instance you naughty
    little devil child!""",
            "Every name is called a * as field and fountain street and town",
            """In place of the noun the * stands as he and she can clap their
    hands""", "The * describes a thing as magic wand or bridal ring",
            """The * means action something done to read, to write, to jump,
    to run""",
            "How things are done the * tells as quickly, slowly, badly, well",
            "The * shows relation as in the street or at the station",
            "* join in many ways sentences, words, phrase, and phrase",
            "Three little words you often see are * a, an, and the",
            "The * cries out hark! We need an exclamation mark",
            "A type of exaggeration used in literature.",
            """A type of figurative imagery using like, as, or than to compare
    two separate items with one another""",
            "Saying something that is different from what you really mean",
            "Using words that end in the same sounds",
            "Repeating something to emphasize it",
            """A series of words, connected in meaning and image which
    emphasize a point""", "Using irony as a attack",
            "A command to the reader or listener"
        ],
        [
            "How many credits does a Level 1 student in 2020 need:",
            "How many credits will a Level 2 student need next year:",
            "The Great Depression started in", "Obsidian is a type of",
            "Hyperinflation is when", "The proper name of America is",
            "Woodrow Wilson was", "Team Fortress 2 is the", "Mein Kampf is",
            "The Great Depression was caused by", "Armistice is",
            """What are the three types of texts in the english external
    unfamiliar texts""", "a NSN is a what", "A 747 is a famous",
            "How much water should you drink in a day",
            "Angles on the same arc",
            """If the angle at the center of a circle is 180° the angle at the
    circumference equals""", "alternate angles on parallel lines",
            "corresponding angles on parallel lines",
            "Two radii in a circle will form what"
        ]
    ]
    quiz_answers = [
        [['n - 2 * 180', '(n - 2)180', 'n - 2 * 60', '360', 1],
         ['n * 60', 'n + 3 * 180', '(n + 3)180', '360', 3],
         ['15', '30', '100', '90', 3],
         ['x = (-3/10) OR x = 3', 'x = 7', 'x = 3', '(10x + 3)(x - 3) = 0', 0],
         [
             '(36x-23)/(12)', '(3(8x - 1) + 4(3x - 5))/(12)', '(3x)/(x-3)',
             '(24x - 3 + 12x - 20)/(12)', 0
         ],
         [
             '(36x-23)/(12)', '(3x(x + 3))/((x+3)(x - 3))', '(3x)/(x-3)',
             '(x - 3)/(3x)', 2
         ],
         [
             'k = √((4d² + 9c²)/(f - 16g))', 'k = (4d² + 9c²)/(f - 16g)',
             'k = √(4d² + 9c²)', 'k = 4d² + 9c² - f - 16g', 0
         ], ['15', '20', '12', '8', 0], ['15', '45', '75', '125', 3],
         [
             'Sin', 'Sine', 'Sine Over Hypotenuse', 'Sine Opposite Hypotenuse',
             3
         ],
         [
             'Cos', 'Cosine Adjacent Hypotenuse', 'Cosine',
             'Cosine Against Hypotenuse', 1
         ],
         [
             'Tan', 'Tangent Over Hypotenuse', 'Tangent Opposite Hypotenuse',
             'Tangent', 2
         ], ['120°', '180°', '360°', 'Three', 1],
         ['360°', '180°', '120°',
          'Five', 0],
         ['add to 180°', 'are equal', 'add to 360°', 'are not related', 1],
         ['Add to 180°', 'Equals 360°', 'Equals 180°', 'Add to 360°', 0],
         ['Add to 180°', 'Equals 360°', 'Equals 180°', 'Add to 360°', 3],
         [
             '120°', 'The sum of the two opposite angles',
             '180° - the opposite angles', '360° - the opposite angles', 1
         ],
         [
             'The base angles are equal', 'The base angles add to 180°',
             'The base angles - 360° equals 180°',
             'The base angles are in a romantic relationship', 0
         ],
         [
             'Are equal', 'Add to 120°', 'Have no relationship', 'Add to 180°',
             3
         ]],
        [['Noun', 'Verb', 'Adjective', 'Adverb', 1],
         ['Hyperbole', 'Rhetoric', 'Imperative', 'Sonnet', 2],
         ['Sonnet', 'Haiku', 'Limerick', 'Free verse',
          1],
         ['Verb', 'Adverb', 'Noun', 'Field',
          2], ['clap', 'Article', 'Adverb', 'Pronoun',
               3], ['Adjective', 'Magic', 'Conjunction', 'Pronoun', 0],
         ['Verb', 'Adverb', 'Noun', 'Read',
          0], ['Quickly', 'Verb', 'Adverb', 'Noun', 2],
         ['Conjunction', 'Street', 'Preposition', 'Adjective', 2],
         ['Conjunctions', 'Sentences', 'Prepositions', 'Adjectives', 0],
         ['Trains', 'Articles', 'Adverbs', 'Pronouns', 1],
         ['Conjunction', 'Mark', 'Interjection', 'Preposition', 2],
         ['Exaggeration', 'Hyperbole', 'Imagery', 'Metaphor', 1],
         ['Exaggeration', 'Imagery', 'Metaphor', 'Simile', 3],
         ['Irony', 'Innuendo', 'Humor', 'Metaphor', 0],
         ['Assonance', 'Rhythm', 'Rhyme', 'Repetition', 2],
         ['Emphasis', 'Listing', 'Repetition', 'Direct speech',
          2], ['Emphasis', 'Listing', 'Repetition', 'Direct speech', 1],
         ['Irony', 'Sarcasm', 'Humor', 'Metaphor', 0],
         ['Imperative', 'Direct address', 'Direct speech', 'Fart', 0]],
        [['80', '60', '72', '70', 3], ['80', '60', '72', '52', 1],
         ['1929', '1933', '1923', '1928', 0],
         [
             'Rock', 'Glass', 'Volcanic Glass',
             'Block used to make a nether portal', 2
         ],
         [
             'The value of a local currency quickly lowers',
             'The gas content of a stomach rapidly increases',
             "A country rapidly enlarges it's borders",
             "Too many people start to work at McDonald's™", 0
         ], ['The United States of America', 'We The People', 'USA', 'US', 0],
         [
             'A famous actor', 'A common name', 'A famous celebrity',
             'The president of The United States of America (POTUS)', 3
         ],
         [
             'Best game in existence', 'Has been in development for 19 years',
             'And is not dead', 'All of the above', 3
         ],
         [
             'German', 'A book written by Hitler',
             'A book written by Woodrow Wilson', 'A famous piece of paper', 1
         ],
         [
             'Hyperinflation', 'Mein Kampf', 'Hitler', 'The Wall Street Crash',
             3
         ],
         [
             'An agreement in a war to stop fighting',
             'A form of jointed club', 'A type of business deal',
             'The name for a yellow carrot', 0
         ],
         [
             'Story, poem and fiction',
             'Narrative prose, poetry and non-fiction',
             'fiction, poetry and non-fiction',
             'aggressive, assertive and passive', 1
         ],
         [
             'National Steward Number', 'iNternational Scalene Nonagon',
             'New South Nales', 'National Student Number', 3
         ], ['Boat', 'Airbus Plane', 'Boeing Plane', 'Rifle', 2],
         [
             '2 Liters', '1.5 Liters', "Enough so that you aren't thirsty",
             'How much you friends drink', 2
         ], ['are 180°', 'add to 180°', 'are equal', 'add to 120°', 2],
         ['80°', '50°', '180°', '90°', 3],
         [
             'Are equal', 'Add to 120°', 'Have no relationship', 'Add to 180°',
             0
         ],
         [
             'Are equal', 'Add to 120°', 'Have no relationship', 'Add to 180°',
             0
         ],
         [
             'A parallelogram', 'A polygon', 'A isosceles triangle',
             'A scalene triangle', 2
         ]]
    ]
    # get the question answer, and score values to use based on the users
    # location
    current_questions = quiz_questions[location - 1]
    current_answers = quiz_answers[location - 1]
    score[location - 1] = 0
    while len(current_questions) > 5:
        # Run while there are still questions left
        rand_choice = rand(0, len(current_questions) - 1)
        # pick a random question and answer
        user_input = None
        while user_input not in (1, 2, 3, 4):
            try:
                user_input = int(
                    input(f"""
    {current_questions[rand_choice]}
    1) {current_answers[rand_choice][0]}
    2) {current_answers[rand_choice][1]}
    3) {current_answers[rand_choice][2]}
    4) {current_answers[rand_choice][3]}
    [1-4]: """))  # give the user the randomly selected question and possible
                # answers
            except ValueError:  # if the user doesn't put in an interger, skip
                # the question and give them the error message
                user_input = None  # set user_input so the program doesn't
                # break delete the question from the master list, and take
                # user input
            if user_input not in (1, 2, 3, 4):
                out_of_range_error(4)
        # get the answers to the randomly selected question
        if user_input - 1 == current_answers[rand_choice][4]:
            input("""
    You got it right""")
            score[location - 1] += 1
        else:
            input(f"""
    You got it wrong.
    The answer was:
    {current_answers[rand_choice][current_answers[rand_choice][4]]}""")
        current_questions.pop(rand_choice)
        current_answers.pop(rand_choice)
    return score


if __name__ == "__main__":
    print(quiz(int(input()), [None, None, None]))
