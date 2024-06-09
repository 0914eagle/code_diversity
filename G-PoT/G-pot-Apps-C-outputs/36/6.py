
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
sorted_bottles = sorted(zip(a, b), key=lambda x: x[1])

min_bottles = 1
min_time = total_soda

for i in range(n):
    remaining_soda = total_soda
    time = 0
    bottles_needed = 0
    for j in range(i, n):
        if remaining_soda <= sorted_bottles[j][1]:
            bottles_needed += 1
            time += remaining_soda
            break
        else:
            bottles_needed += 1
            time += sorted_bottles[j][0]
            remaining_soda -= sorted_bottles[j][0]
    
    if bottles_needed < min_bottles or (bottles_needed == min_bottles and time < min_time):
        min_bottles = bottles_needed
        min_time = time

print(min_bottles, min_time)
