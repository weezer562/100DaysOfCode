logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
print("Welcome to the Caesar Cipher Program")

def encode(text, shift):
    print("Your encoded text is: ")
    encoded_text = ""

    for letter in text:
        encoded_text += chr(ord(letter) + shift)
        
    print(encoded_text)


def decode(text, shift):
    print("Your decoded text is: ")

    decoded_text = ""

    for letter in text:
        decoded_text += chr(ord(letter) - shift)
        
    print(decoded_text)

again = True

while again:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    if choice.lower() == 'encode':
        encode(text, shift)
    elif choice.lower() == 'decode':
        decode(text, shift)
    else:
        print("Invalid choice")

    if input("Do you want to go again? (yes/no) ").lower() == "no":
        again = False
        print("Goodbye")
    
    