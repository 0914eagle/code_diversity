
t, n = map(int, input().split())
questions = []
answers = []
for _ in range(n):
    q, a = input().split('?')
    questions.append(q.strip())
    answers.append(a.strip())

total_score = 0
for q, a in zip(questions, answers):
    words = q.split()
    time_to_answer = 1
    for i in range(len(words)):
        if words[i] == a:
            score = 1 / (len(words) - i)
            total_score += score
            break

print("{:.10f}".format(total_score))
