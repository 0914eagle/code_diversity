
t, n = map(int, input().split())
total_score = 0

for _ in range(n):
    question, answer = input().split('?')
    words = question.split()
    
    for i in range(len(words)):
        partial_question = ' '.join(words[:i+1]) + '?'
        if partial_question == answer:
            total_score += 1
            break

expected_score = total_score / n
print("{:.10f}".format(expected_score))
