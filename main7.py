#python quiz game

questions = ("Elements in periodic table?",
             "Animal with the largest eggs?",
             "Most abundant gas on earth?",
             "Bones in human body",
             "Hottest planet in solar system?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Bat", "B. Bear", "C. Cat", "D. Dog"),
           ("A. Helium", "B. Nitrogen", "C. Oxygen", "D. Argon"),
           ("A. Bones", "B. Skin", "C. Flesh", "D. Muscle"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong answer!")
        print(f"{answers[question_num]} is correct answer")
    question_num += 1

print("------------------")
print("----Results--------")
print(f"You got {score} out of 5 questions correct")
