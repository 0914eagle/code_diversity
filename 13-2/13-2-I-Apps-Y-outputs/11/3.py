
import sys

n, k = map(int, input().split())
sticks = list(map(int, input().split()))

sticks.sort()

max_length = 0
for i in range(k):
    max_length += sticks[i]

print(max_length)

