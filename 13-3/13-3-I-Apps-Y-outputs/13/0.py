
A, P = map(int, input().split())

# Calculate the maximum number of apple pies we can make
max_pies = A // 3
if P >= 2:
    max_pies += A // 6

print(max_pies)

