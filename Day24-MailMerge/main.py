NAMES_PATH = "Input/Names/invited_names.txt"
DEFAULT_LETTER_PATH = "Input/Letters/starting_letter.txt"


def create_letters():
    names = open(NAMES_PATH).read().split("\n")

    for name in names:
        with open(DEFAULT_LETTER_PATH, "r") as file:
            default_text = file.read()

        updated_text = default_text.replace("[name]", name)

        save_path = f"Output/ReadyToSend/letter_for_{name}"
        with open(save_path, "w") as file:
            file.write(updated_text)


create_letters()
