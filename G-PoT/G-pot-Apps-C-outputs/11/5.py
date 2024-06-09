
t, n = map(int, input().split())
total_score = 0

for _ in range(n):
    question, answer = input().split('?')
    words = question.split()
    
    if answer in words:
        total_score += 1
    else:
        total_score += 1 / (len(words) + 1)

expected_score = total_score / n
print("{:.10f}".format(expected_score))
