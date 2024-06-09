
import sys

N = int(input())
T = input()

# Concatenate 10^10 copies of 110
S = '110' * (10**10)

# Count the number of occurrences of T in S
count = 0
for i in range(len(S) - len(T) + 1):
    if S[i:i+len(T)] == T:
        count += 1

print(count)

