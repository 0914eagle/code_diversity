
import sys

t, n = map(int, input().split())

total_score = 0
for _ in range(n):
    question, answer = input().split('?')
    words = question.split()
    
    possible_answers = 0
    correct_answers = 0
    
    for i in range(len(words)):
        possible_answers += 1
        if words[i] == answer:
            correct_answers += 1
            total_score += 1
        
        expected_score = correct_answers / possible_answers
        
        if expected_score * (len(words) - i) <= t:
            total_score += expected_score * (len(words) - i)
            break

print("{:.10f}".format(total_score))
