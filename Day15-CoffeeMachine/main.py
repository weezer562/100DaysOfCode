import menu

def get_coffee(choice):
    """Returns chosen coffee"""
    return menu.MENU.get(choice)

def check_resources(name, coffee, resources):
    """Checks if enough ingredients exist to make the coffee, returns bool"""
    if coffee["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif name != "espresso":
        if coffee["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
    elif coffee["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    
    return True

def update_resources(choice, drink, resources):
    resources["water"] -= drink["ingredients"]["water"]
    resources["coffee"] -= drink["ingredients"]["coffee"]
    
    if choice != "espresso":
        resources["milk"] -= drink["ingredients"]["milk"]
    
        
def print_report(resources, money):
    print(f"water: {resources["water"]}")
    print(f"milk: {resources["milk"]}")
    print(f"coffee: {resources["coffee"]}")
    print(f"money: {money}")
    
def check_money(due, money_received):
    """Checks money paid until money is returned"""
    owe = True
    while owe:
        difference = due - money_received
        
        if money_received == due:
            owe = False
        elif money_received < due:
            print(f"You don't have enough money, missing ${format(difference, '.2f')}.")
            choice = input("Add more money? (a) or refund? (r): ").lower()
            
            if choice == "a":
                money_received += float(input("How much to add? $"))
                continue
            elif choice == "r":
                print(f"Refunded: ${format(money_received, '.2f')}")
                return False
        elif money_received > due:
            print(f"Here is your change, ${format(money_received-due, '.2f')}")
            return False
                
        return True

def coffee_machine():
    choose_coffee = True
    money = 0.0
    
    while choose_coffee:
        coffee_choice = input("What Coffee would you like (Latte, Cappuccino, Espresso) ").lower()
        
        if coffee_choice == "off":
            choose_coffee = False
            break
        elif coffee_choice == "report":
            print_report(resources, money)
            continue
        elif coffee_choice not in menu.MENU:
            print(f"Sorry we do not serve {coffee_choice}.")
            continue
        
        resources = menu.resources
        
        coffee = get_coffee(coffee_choice)
        
        if not check_resources(coffee_choice, coffee, resources):
            continue
        
        money_tendered = float(input(f"You owe ${format(coffee["cost"], '.2f')}. Enter pay amount $"))
        due = coffee["cost"]
        
        complete = check_money(due, money_tendered)
            
        if complete:
            print(f"Here is your {coffee_choice}")
            
            money += coffee["cost"]
            update_resources(coffee_choice, coffee, resources)
            
    print("Turning off coffee machine......")
    
    
coffee_machine()