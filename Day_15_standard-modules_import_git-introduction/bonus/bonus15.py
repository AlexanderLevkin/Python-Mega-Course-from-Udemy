import json

with open("queation.json") as json_file:
    content = json_file.read()

data = json.loads(content)
print(data)

for question in data:
    print(question["quastion_text"] + "\n")
    for index, alternative in enumerate(question["alternatives"]):
        print(f"\t{index + 1} - {alternative}")
    user_answer = int(input("Your answer: "))
    question["user_answer"] = user_answer

score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer!"
    else:
        result = "Wrong Answer!"
    message = f"{result} {index + 1} - Your question is {question['user_answer']}, Correct answer: " \
              f"{question['correct_answer']}"
    print(message)
print(f"Your score is {score}/{len(data)}")
