
n = int(input())
remaining_soda = list(map(int, input().split()))
bottle_volumes = list(map(int, input().split()))

total_soda = sum(remaining_soda)
sorted_bottles = sorted(zip(remaining_soda, bottle_volumes), key=lambda x: x[1])

min_bottles = 1
min_time = total_soda

for i in range(n):
    soda = 0
    time = 0
    for j in range(i, n):
        soda += sorted_bottles[j][0]
        time += sorted_bottles[j][1] - sorted_bottles[j][0]
        if soda >= total_soda:
            if time < min_time or (time == min_time and j - i + 1 < min_bottles):
                min_bottles = j - i + 1
                min_time = time
            break

print(min_bottles, min_time)
