class QuizBrain():
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
        self.incor_ans = []

    def check_ans(self, user_choose,answer, cur_ques):
        if (user_choose == answer):
            self.score += 1
            print("Correct choice. Congratulation")
        else:
            self.incor_ans.append(cur_ques)
            print("that's wrong. Keep try ")
        print(f"Your current score is {self.score}/ {self.question_number}\n\n")


    def next_q(self):
        cur_ques = self.question_list[self.question_number]
        self.question_number +=1
        print(f"Q.{self.question_number} ")
        print(f"Category: {cur_ques.category}")
        print(f"Type: {cur_ques.type}")
        print(f"Difficulty: {cur_ques.difficulty}")
        print(f"Question: {cur_ques.question}")
        user_choose = input("Type your answer: true or false:   ").lower()
        answer = cur_ques.correct_answer.lower()
        self.check_ans(user_choose, answer, cur_ques)

    def still_has_ques(self):
        return self.question_number < len(self.question_list)

    def print_result(self):
        print(f"Your final score is : {self.score} / {self.question_number}")
        print("Your list incorrect answer: ")
        for item in self.incor_ans:
            print(f"***. {item.question} ")
            print(f"Correct answer is: {item.correct_answer} \n")
