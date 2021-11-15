from question import Question

score = 0

question_prompts = [
    "When a volcano wakes up, we say that it...\nA: Erupts\nB: Irrupts\nC: Interrupts\nD: Explodes",
    "\nWho shall not be named?\nA: Venom\nB: Vernon\nC: Voldemort\nD: Vol'jin",
    "\nWhat is the name of the blue cartoon tank engine?\nA: Trevor\nB: Thomas\nC: Tony\nD: Timothy"
]

questions = [
    Question(question_prompts[0], "A"),
    Question(question_prompts[1], "C"),
    Question(question_prompts[2], "B")
]

for question in questions:
    print(question.prompt)

    answer = input("> ")

    if answer.upper() == question.answer:
        print("\nCorrect!")

        score += 1
    else:
        print("\nSorry, wrong answer!")

print("\nYou got " + str(score) + " out of " + str(len(question_prompts)) + " correct!")
