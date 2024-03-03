while True:
    print("Welcome to the tip calculator.")
    
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    tip = total_bill * (tip_percentage / 100)
    total = total_bill + tip
    each_person = total / people

    print(f"Each person should pay: ${round(each_person, 2)}")
    
    print("Would you like to calculate another bill? (yes/no)")
    another = input()
    if another == "no":
        break
    else:
        continue

