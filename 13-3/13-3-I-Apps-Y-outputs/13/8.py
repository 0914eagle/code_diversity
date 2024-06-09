
A, P = map(int, input().split())

max_pies = 0
while A >= 2:
    max_pies += A // 2
    A = A % 2 + A // 2

print(max_pies + P)

