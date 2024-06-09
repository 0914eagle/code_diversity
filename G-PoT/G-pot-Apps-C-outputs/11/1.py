
t, n = map(int, input().split())
questions = []
answers = []
for _ in range(n):
    question, answer = input().split('?')
    questions.append(question.strip())
    answers.append(answer.strip())

total_score = 0
for i in range(n):
    question_words = questions[i].split()
    correct_answer = answers[i]
    max_score = 0
    for j in range(len(question_words)):
        if question_words[j] == correct_answer:
            max_score = max(max_score, j + 1)
    total_score += max_score / len(question_words)

expected_score = total_score / n
print("{:.10f}".format(expected_score))
