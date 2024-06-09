
import sys

A, B, C = map(int, input().split())

if A + B + C == 16 and A <= 10 and B <= 10 and C <= 10:
    print("YES")
else:
    print("NO")

