
n = int(input())
remaining_soda = list(map(int, input().split()))
bottle_volume = list(map(int, input().split()))

total_soda = sum(remaining_soda)
sorted_bottles = sorted(zip(remaining_soda, bottle_volume), key=lambda x: x[1])

min_bottles = 1
min_time = total_soda

for i in range(n):
    soda_needed = total_soda - sum(x[0] for x in sorted_bottles[:i])
    time_needed = sum(min(x[1] - x[0], soda_needed) for x in sorted_bottles[:i])
    
    if time_needed < min_time:
        min_time = time_needed
        min_bottles = i + 1

print(min_bottles, min_time)
