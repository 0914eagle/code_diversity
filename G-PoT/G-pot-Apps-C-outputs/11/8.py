
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
    time_to_answer = len(words) + 1  # Time to answer is number of words + 1 second
    score_if_answered = 1
    score_if_not_answered = 0
    for i in range(len(words)):
        if words[i] == a:
            score_if_not_answered += 1
            score_if_answered = max(score_if_answered, score_if_not_answered)
        else:
            score_if_not_answered = max(score_if_not_answered, score_if_answered)
    total_score += max(score_if_answered, score_if_not_answered)

expected_score = total_score / n
print("{:.10f}".format(expected_score))
