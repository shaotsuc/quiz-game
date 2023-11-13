from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question( question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)
quiz.next_question()