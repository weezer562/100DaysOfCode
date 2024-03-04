import random

rock = '''    
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    
_______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)'''

scissors = '''    
_______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)'''

while True:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

    if choice == "0":
        print("You show:\n" + rock)
    elif choice == "1":
        print("You show:\n" + paper)
    elif choice == "2":
        print("You show:\n" + scissors)
    else:
        print("Invalid input. You lose.")

    aiChoice = str(random.randint(0, 2))
    if aiChoice == "0":
        print("AI shows:\n" + rock)
    elif aiChoice == "1":
        print("AI shows:\n" + paper)
    else:
        print("AI shows:\n" + scissors)

    # 0 = rock, 1 = paper, 2 = scissors
    # rock > scissors, scissors > paper, paper > rock
    if choice == aiChoice:
        print("It's a draw.")
    # rock < paper
    elif choice == "0" and aiChoice == "1":
        print("You lose.")
    # paper < scissors
    elif choice == "1" and aiChoice == "2":
        print("You lose.")
    # scissors < rock
    elif choice == "1" and aiChoice == "2":
        print("You lose.")
    else:
        print("You win.")


      