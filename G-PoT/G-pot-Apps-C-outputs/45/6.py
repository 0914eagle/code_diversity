
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    if M == 0 or N == 2:
        print("First")
    else:
        print("Second")
