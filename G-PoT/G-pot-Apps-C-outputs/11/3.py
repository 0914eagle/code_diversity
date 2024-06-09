
import sys

t, n = map(int, input().split())
questions = []
answers = []

for _ in range(n):
    q, a = input().split('?')
    questions.append(q.strip())
    answers.append(a.strip())

total_score = 0
for i in range(n):
    q = questions[i].split()
    a = answers[i]

    time_to_answer = 1
    for j in range(len(q)):
        if q[j] == a:
            score = 1 / (len(q) - j)
            total_score += score
            break
        time_to_answer += 1

        if time_to_answer >= t:
            break

print("{:.10f}".format(total_score))
