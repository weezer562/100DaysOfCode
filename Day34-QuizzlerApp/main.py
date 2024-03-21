from data import Data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
questions = Data()
for question in questions.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
