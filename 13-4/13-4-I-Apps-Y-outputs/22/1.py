
import sys

A, B, C, K = map(int, input().split())

# Calculate the maximum sum by considering all possible combinations of cards
max_sum = 0
for i in range(K+1):
    for j in range(K+1-i):
        current_sum = i * 1 + j * 0 + (K-i-j) * -1
        max_sum = max(max_sum, current_sum)

print(max_sum)

