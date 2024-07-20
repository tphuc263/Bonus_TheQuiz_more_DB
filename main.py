from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

quiz_list = []
for item in question_data:
    category = item["category"]
    type = item["type"]
    difficulty = item["difficulty"]
    ques = item["question"]
    correct_ans = item["correct_answer"]
    incorrect_ans_list = item["incorrect_answers"]
    question = Question(category, type, difficulty, ques, correct_ans, incorrect_ans_list)
    quiz_list.append(question)

quiz_game = QuizBrain(quiz_list)
while quiz_game.still_has_ques():
    quiz_game.next_q()


quiz_game.print_result()
