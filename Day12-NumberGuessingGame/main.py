import random

def set_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if choice.lower() == "easy":
        return 10
    elif choice.lower() == "hard":
        return 5
    else:
        print("Invalid choice")
        keep_guessing = False
    

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
    
    if guess == random_number:
        win = True
        break
    if guess > random_number:
        print("Too high")
    elif guess < random_number:
        print("Too Low")
    else:
        print("Guess again.")

    guesses -= 1
        
if win:
    print(f"You got it! The answer was {random_number}.")
elif not win:
    print("You've run out of guesses, you lose.")