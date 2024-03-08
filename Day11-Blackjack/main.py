import os
import random
import time


bj_logo = """"88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  """""

suites = {
    "Hearts": "\u2665",
    "Clubs": "\u2663",
    "Diamonds": "\u2666",
    "Spades": "\u2660",
}

card_values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

default_deck = {}
deck = {}

def deal_card():
    """Deals a card from generated deck, and removes it.

    Returns:
        _type_: string
    """
    card = random.choice(list(deck.items()))[0]
    deck.pop(card, None)
    return card

def getDeck():
    """Returns a new full 52 card deck.

    Returns:
        _type_: dictionary
    """
    for num in range(2, 15):
        for suite in suites:
            if num > 10 and num < 14:
                deck[f"{card_values[num-2]}{suites[suite]}"] = 10
            elif num == 14:
                deck[f"{card_values[num-2]}{suites[suite]}"] = 11
            else: 
                deck[f"{num}{suites[suite]}"] = num
        
    return deck

def printCards(cards):
    """Prints out desired hand.

    Args:
        cards (_type_): string
    """
    for card in cards:
        print(card, end=" ")
        
    print()
        
def getTotal(hand):
    """Returns hand total.

    Args:
        hand (_type_): list of strings

    Returns:
        _type_: int
    """
    total = 0
    for card in hand:
        total += default_deck[card]
        if card.startswith('A') and total > 21:
            total -= 10
    return total
    
def print_decks(status, wait_time):
    """Prints status of game and both player hands

    Args:
        status (_type_): string
        wait_time (_type_): int
    """
    os.system('cls' if os.name == "nt" else 'clear')
    print(status)
    print(f"Computer Total: {getTotal(computerCards)}")
    printCards(computerCards)

    print(f"Player Total: {getTotal(playerCards)}")
    printCards(playerCards)
    time.sleep(wait_time)

def blackjack_check(deck):
    """Check for blackjack

    Args:
        deck (_type_): list of strings

    Returns:
        _type_: bool
    """
    blackjack = False
    has_ace = any(card.startswith('A') for card in deck)
    has_face_card = any(card.startswith(('J', 'Q', 'K')) for card in deck)
    
    if has_ace and has_face_card:
        blackjack = True
    return blackjack

os.system('cls' if os.name == "nt" else 'clear')
print(bj_logo)

play = input("Would you like to play Blackjack? (y/n) ")
again = True

if play.lower() != "y":
    again = False

while again:
        
    print("Welcome to blackjack!\n")
    # Create new deck
    getDeck()

    # copy deck for card removal
    default_deck = deck.copy()

    # set Player and computer decks
    playerCards = []
    computerCards = []

    player_total = 0
    computer_total = 0

    # Add initial 2 cards for player
    playerCards.append(deal_card())
    playerCards.append(deal_card())

    # Deal one compuyter card
    computerCards.append(deal_card())

    hit = True
    hit = not blackjack_check(playerCards) # skip loop if player has blackjack

    print_decks("Dealing cards....", 1)

    while hit:
        choice = input("Hit? (y/n) ")
        
        if choice.lower() == "n":
            hit = False
            break    
        
        card = deal_card()
        playerCards.append(card)
    
        print_decks(f"You draw a {card}.", 1) 
        
        player_total = getTotal(playerCards)
    
        if player_total > 21:
            break
        
    card = deal_card()
    computerCards.append(card)

    print_decks("Computer flips second card.......", 1)

    computer_total = getTotal(computerCards)
    player_total = getTotal(playerCards)

    if blackjack_check(playerCards) : # Player wins if it has blackjack
        print_decks("You Win. BlackJack!!", 1)
    elif blackjack_check(computerCards): # Computer wins if it has blackjack
        print_decks("You lose. Computer has Blackjack")
    elif player_total > 21:  # Player bust over 21
        print_decks("You Bust!!", 0)
    else:
        while computer_total < 21:    
            card = deal_card()
            computerCards.append(card)
            computer_total = getTotal(computerCards)
            
            print_decks(f"Computer draws {card}", 2)
            
            if computer_total > 21: # Computer bust if draw  over 21
                print_decks("You Win. Computer Bust!!", 1)
                break
            elif computer_total == player_total: # Draw game if matching total
                print_decks("Push, no one wins", 1)
                break
            elif computer_total >= 16:  # Computer holds at 16
                if computer_total > player_total:
                    print_decks("You Lose. Computer Wins!!", 0)
                    break
            elif computer_total < player_total: # Computer wins once they > player but < 21
                print_decks("You lose. Computer wins!!", 1)
                break
            else: 
                print_decks("You Lose", 0)
        
    choice = input("Play again? (y/n) ")
    if choice != "y":
        again = False
        


    
