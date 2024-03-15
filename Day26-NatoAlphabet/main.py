import pandas

# Read File and covert to dictionary {"A": "Alpha", "B"......}
file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in file.iterrows()}

# Get user input and split word into a list
user_word = input("Enter a word: ")

word_list = [nato_dict[letter.upper()] for letter in user_word]
print(word_list)
