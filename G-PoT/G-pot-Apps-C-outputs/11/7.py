
import sys

t, n = map(int, input().split())
questions = []
answers = []

for _ in range(n):
    q, a = input().split("? ")
    questions.append(q + "?")
    answers.append(a)

total_score = 0
for q, a in zip(questions, answers):
    words = q.split()
    score_if_answer = 0
    score_if_wait = 0
    for i in range(len(words)):
        if words[i] == a:
            score_if_answer = 1 + (i / len(words))
            break
        score_if_wait = 1 + (i / len(words))
    
    total_score += max(score_if_answer, score_if_wait)

print("{:.10f}".format(total_score))
