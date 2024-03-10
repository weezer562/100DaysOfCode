import random

def set_difficulty():
    """Sets game difficulty, easy 10 guesses, hard 5 guesses

    Returns:
        _type_: int
    """
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if choice.lower() == "easy":
        return 10
    elif choice.lower() == "hard":
        return 5
    else:
        print("Invalid choice")
        keep_guessing = False
        
def win_check(guess, random_number, guesses):
    """Check if guess matches

    Args:
        guess (_type_): string
        random_number (_type_): int
        guesses (_type_): int

    Returns:
        _type_: int
    """
    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        return -1
    if guess > random_number:
        print("Too high")
        guesses -= 1
        return guesses
    elif guess < random_number:
        print("Too Low")
        guesses -= 1
        return guesses

def guessing_game():
    """Guessing Game Start"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1,101)
    keep_guessing = True
    guesses = set_difficulty()

    while keep_guessing:
        
        win = False
        
        if guesses == 0:
            break
        
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))\
        
        guesses = win_check(guess, random_number, guesses)
        
        if guesses == -1:
            break
        elif guesses == 0:
            print(f"You ran out of guesses. The number was {random_number}")
          
guessing_game()