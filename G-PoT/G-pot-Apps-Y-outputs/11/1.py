
A, B = map(int, input().split())

if (A + B) % 2 == 0:
    K = (A + B) // 2
    print(K)
else:
    print("IMPOSSIBLE")
