import random

def user_guess_number(x: int) -> None:
    """
    Guess a random number between 1 and x (inclusive).

    Parameters:
        x (int): The upper limit of the range to guess from.

    Returns:
        string of the random number and the number of times
          it takes to get the guess
    """
    random_number = random.randint(1, x)
    guess_number = 0
    trials = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))
        trials += 1
        if guess_number > random_number:
            print("Sorry, guess again. Too high")
        elif guess_number < random_number:
            print("Sorry, guess again. Too low")

    print(f"You guessed the number {random_number} correctly after {trials} trials")

def comp_guess_number(x):
    """
    Set a random number between 1 and x (inclusive).

    Parameters:
        x (int): The upper limit of the range to guess from.

    Returns:
        print statement of the randomly generated number and the number of trials it took the computer to guess it.
    """
    low = 1
    high = x
    feedback = ""
    trials = 0
    while feedback != "c":
        trials += 1
        if low != high:
            comp_guess = random.randint(low, high)
        else:
            comp_guess = low
        feedback = input(f"Is {comp_guess} too high (H), too low (L) or correct (C) ").lower()
        if feedback == "h":
            high = comp_guess - 1
        elif feedback == "l":
            low = comp_guess + 1
    
    print(f"The computer have guess the number {comp_guess} correctly after {trials} trials")

comp_guess_number(1000)