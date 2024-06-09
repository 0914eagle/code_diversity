
n, d_m = map(int, input().split())
d_values = list(map(int, input().split()))

k = 0
for i in range(1, n):
    if d_values[i] > d_m:
        k += 1
    else:
        break

if k > 0:
    print(f"It hadn't snowed this early in {k} years!")
else:
    print("It had never snowed this early!")
