
import sys

n = int(input())
lengths = list(map(int, input().split()))

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if lengths[i] != lengths[j] != lengths[k] != lengths[i]:
                if is_triangle(lengths[i], lengths[j], lengths[k]):
                    count += 1

print(count)

