
t, n = map(int, input().split())
total_score = 0

for _ in range(n):
    question, answer = input().split('?')
    words = question.split()
    
    for i in range(len(words)):
        if words[i] == answer:
            score = i + 1
            total_score += 1 / (len(words) - score + 1)

print("{:.10f}".format(total_score))
