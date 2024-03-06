gavel_logo = """
        ___________
           /         /
          )_______(
          |"""""""|_.-._,.---------.,_.-._
          |       | | |               | | ''-.
          |       |_| |_             _| |_..-'
          |_______| '-' `'---------'` '-'
          )"""""""(
         /_________\\
        `'-------'`
     .-------------.
    /_______________\""""

print(gavel_logo)

print("Welcome to the Secret Auction Program")

more_bidders = True
bidders = {}

while more_bidders:
    person = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidders[person] = bid
    
    more = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if more != 'yes':
        more_bidders = False

highest_bid = 0

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")


