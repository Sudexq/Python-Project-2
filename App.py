from Question import Question

question_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange",
    "\nWhat color are bananas?\n(a) White\n(b) Black\n(c) Yellow",
    "\nWhat color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
]


def run_test(questions):
    score = 0
    for q in range(len(questions)):
        answer = input(questions[q].prompt +"\nEnter your answer: ")
        if answer == questions[q].answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)