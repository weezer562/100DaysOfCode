# basic way to generate each digit in a row
# Could simply create password and then .shuffle list
import random

print("Welcome to the PyPasswrord Generator!")

numberLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like?\n"))
numNumbers = int(input("How many numbers would you like?\n"))

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+"

passwordTotalLength = numberLetters + numSymbols + numNumbers

password = ""

for i in range(0, passwordTotalLength):
    cType = random.choice([0, 1, 2])  # 0 = letter, 1 = symbol, 2 = number

    if numberLetters == 0:
        cType = random.choice([1, 2])
    elif numSymbols == 0:
        cType = random.choice([0, 2])
    elif numNumbers == 0:
        cType = random.choice([0, 1])
    elif numberLetters == 0 and numSymbols == 0:
        cType = 2
    elif numberLetters == 0 and numNumbers == 0:
        cType = 1
    elif numSymbols == 0 and numNumbers == 0:
        cType = 0
    elif numberLetters == 0 and numSymbols == 0 and numNumbers == 0:
        break
  
    # letter
    if cType == 0:
        letterCase = random.randint(0, 1) # 0 = uppercase, 1 = lowercase
        newLetter = random.choice(letters)
        if letterCase == 1:
            password += newLetter.lower()
            numberLetters -= 1
        else:
            password += newLetter
            numberLetters -= 1
    # symbol 
    elif cType == 1:
        password += random.choice(symbols)
        numSymbols -= 1
    # number
    elif cType == 2:
        password += random.choice(digits)
        numNumbers -= 1
    elif cType == 3:
        password += random.choice(digits)
        numNumbers -= 1

print(f"Here is your password: {password}")