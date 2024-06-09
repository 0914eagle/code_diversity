
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
sorted_bottles = sorted(zip(a, b), key=lambda x: x[1])

k = 1
t = total_soda
current_soda = 0

for i in range(n):
    current_soda += sorted_bottles[i][0]
    if current_soda >= total_soda - current_soda:
        k = i + 1
        t = max(current_soda, total_soda - current_soda)
        break

print(k, t)
