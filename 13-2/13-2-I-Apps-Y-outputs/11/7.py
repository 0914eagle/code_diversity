
import sys

n, k = map(int, input().split())
lengths = list(map(int, input().split()))

lengths.sort()

max_length = 0
for i in range(k):
    max_length += lengths[i]

print(max_length)

