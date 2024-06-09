
import sys

N = int(input().strip())
L = list(map(int, input().strip().split()))

def is_triangle(a, b, c):
    return a**2 + b**2 > c**2

def count_triangles(L):
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k]:
                    if is_triangle(L[i], L[j], L[k]):
                        count += 1
    return count

print(count_triangles(L))

