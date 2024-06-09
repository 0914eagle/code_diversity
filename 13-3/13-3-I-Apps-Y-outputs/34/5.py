
A, B, C = map(int, input().split())
if A + B + C == 16 and A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
    print("YES")
else:
    print("NO")

