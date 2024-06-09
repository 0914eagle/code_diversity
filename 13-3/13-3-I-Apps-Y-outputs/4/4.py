
A, B, C = map(int, input().split())

max_allowance = max(A + B, A + C, B + C)

print(max_allowance)

