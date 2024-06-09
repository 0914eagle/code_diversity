
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
total_bottles = n
time = 0

for i in range(n):
    if a[i] > b[i]:
        time += b[i]
        total_soda -= b[i]
    else:
        time += a[i]

if total_soda > 0:
    for i in range(n):
        if a[i] < b[i]:
            if total_soda <= b[i] - a[i]:
                total_bottles -= 1
                time += total_soda
                break
            else:
                total_bottles -= 1
                time += b[i] - a[i]
                total_soda -= b[i] - a[i]

print(total_bottles, time)
