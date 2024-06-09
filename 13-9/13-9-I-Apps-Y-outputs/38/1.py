
n = int(input())
answers = input().split()
score = 0

for i in range(n):
    if answers[i] == "A":
        score += 1

print(score)

