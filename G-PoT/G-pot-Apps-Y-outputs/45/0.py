
N, P, Q = map(int, input().split())

total_points = P + Q
if total_points // N % 2 == 0:
    print("paul")
else:
    print("opponent")
