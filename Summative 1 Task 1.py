import random  # Random module imported so we can generate random numbers for equations

TOTAL_QUIZ_QUESTIONS = 5  # The quiz's total questions asked to player (will remain constant)

def randomised_equation():
    """
    This function uses the random module to create a equation in the following form, x * y = z, ensuring x and z are random integers
    
    Returns:
        question_equation (str): The equation for the question as a string value
        y_answer (int): The answer to the question as an integer value
    """
    x_coefficient = random.randint(1, 20)  # A randomly created integer assigned to coefficient 'x' of the equation
    y_answer = random.randint(1, 20)  # A randomly created integer for the answer of a quiz question 'y'
    z_result = x_coefficient * y_answer  # result of equation calculated 
    question_equation = f"{x_coefficient} × x = {z_result}"  # Equation formatted as a string
    return question_equation, y_answer  # The question's equation and answer is returned as a tuple

def answer_validation(users_input_value, y_answer):
    """
    This checks if the answer to question matches to the user's inputted value

    Arguments:
        users_input_value (str): The user's input value as a string value
        y_answer (int): The answer to the equation in question as an integer value

    Returns:
        boolean: False if incorrect (do not match), True if correct (match)
    """
    try:
        return int(users_input_value) == y_answer  # User's input value is compared to the correct answer for the question 
    except ValueError:
        return False  # If input is invalid (e.g. an error occurs), a False value is returned

def begin_equation_quiz():
    """
    This begins the equation quiz game, user's points are tracked, and results displayed upon completion.
    """
    user_points = 0

    print("You are about to embark on the mathematical Quiz of a lifetime!")
    print(f"There will be {TOTAL_QUIZ_QUESTIONS} questions.\nTry your best!")
    print("Record your answers below!")

    for a in range(TOTAL_QUIZ_QUESTIONS):
        equation, solution = randomised_equation()
        print(f"Question {a + 1}: {equation}")

        user_input = input("What is your response?: ")
        if answer_validation(user_input, solution):
            print("Fantastic!")
            user_points += 1
        else:
            print(f"Great attempt!\nThe correct answer was {solution}.")

    print("\nYou have reached the end of the Quiz!")
    print(f"You managed to get {user_points}/{TOTAL_QUIZ_QUESTIONS}. Amazing Effort!")


begin_equation_quiz()

