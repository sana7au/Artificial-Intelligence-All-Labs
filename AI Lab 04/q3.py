correct_answers = ["A", "C", "B", "D", "A"]
user_answers = []

def grade_quiz(user_answers, correct_answers):
    score = 0
    attempted = len(user_answers)
    
    for i in range(attempted):
        if user_answers[i] == correct_answers[i]:
            score += 1
    
    if(attempted > 0):
        percentage = float((score / attempted) * 100)
    else:
        percentage = float(0)
    
    return {
        "score": score,
        "attempted": attempted,
        "percentage": percentage
    }

while len(user_answers) < len(correct_answers):
    answer = input(f"Question {len(user_answers) + 1} answer (or 'quit' to stop): ")
    
    if answer == "quit":
        break

    user_answers.append(answer)

result = grade_quiz(user_answers, correct_answers)

print(f"score -> {result['score']}")
print(f"attempted -> {result['attempted']}")
print(f"percentage -> {result['percentage']}")
print("")