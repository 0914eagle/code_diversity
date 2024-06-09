
A, B, C = map(int, input().split())

if A + B + C == 16 and A % 5 == 0 and B % 7 == 0:
    print("YES")
else:
    print("NO")

