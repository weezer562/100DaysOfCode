import os


class IOManager:
    def __init__(self):
        self.file_name = "score.txt"

    def write_to_file(self, score, high_score):
        with open(self.file_name, mode="w") as file:
            file.write(f"{score}\n{high_score}")

    def read_file(self):
        if not os.path.exists(self.file_name):
            self.write_to_file(0, 0)

        with open(self.file_name) as file:
            contents = file.read()
            scores = [int(score) for score in contents.split('\n') if score]
            return scores
