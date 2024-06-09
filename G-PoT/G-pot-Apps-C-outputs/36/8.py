
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
sorted_bottles = sorted(zip(a, b), key=lambda x: x[1])

min_bottles = 1
min_time = total_soda

for i in range(n):
    current_soda = total_soda
    current_time = 0
    for j in range(i, n):
        if current_soda <= sorted_bottles[j][1]:
            current_time += current_soda
            min_bottles = min(min_bottles, n - (j - i + 1))
            min_time = min(min_time, current_time)
            break
        else:
            current_time += sorted_bottles[j][0]
            current_soda -= sorted_bottles[j][1]

print(min_bottles, min_time)
