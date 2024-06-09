
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
sorted_bottles = sorted(zip(a, b), key=lambda x: x[1])

k = 0
t = 0
for soda, volume in sorted_bottles:
    if total_soda <= volume:
        k += 1
        t += soda
        break
    else:
        k += 1
        t += soda
        total_soda -= volume

print(k, t)
