import random
import art
import game_data


def get_person():
    return random.choice(game_data.data)


def print_person(person):
    print(f"Compare A: {person["name"]}, a {person["description"]}, from {person["country"]}")


def check_guess(choice, first, second):
    if first["follower_count"] > second["follower_count"]:
        return choice == "a"
    else:
        return choice == "b"


def higher_lower_game():
    next = True
    score = 0
    print(art.logo)
     
    while True:
        first_person = get_person()
        
        second_person = get_person()
        if second_person == first_person:
            second_person = get_person()
        
        print_person(first_person)
        print(art.vs)
        print_person(second_person)
        
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        next = check_guess(choice, first_person, second_person)
        
        if next:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

higher_lower_game()