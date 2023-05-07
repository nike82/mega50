# a = [{"question_text": "What are dolphins?",
#       "alternatives": ["Amphibians", "Fish", "Mammals", "Birds"],
#       "correct_answer": 3},
#      {"question_text": "What occupies most of the Earth's surface?",
#       "alternatives": ["Land", "Water"],
#       "correct_answer": 2}]

import json

with open("./files/questions.json") as file:
    content = file.read()
data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(f"Your score: {score} / {len(data)}")


