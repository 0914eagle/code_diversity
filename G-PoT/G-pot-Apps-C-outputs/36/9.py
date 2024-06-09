
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
sorted_bottles = sorted(zip(a, b), key=lambda x: x[1])

current_soda = 0
bottles_needed = 0
time_needed = 0

for soda, volume in sorted_bottles:
    if current_soda >= total_soda // 2:
        break
    if current_soda + soda <= volume:
        current_soda += soda
        bottles_needed += 1
        time_needed += soda
    else:
        remaining_soda = total_soda - current_soda
        transfer = min(remaining_soda, volume - current_soda)
        current_soda += transfer
        bottles_needed += 1
        time_needed += transfer

print(bottles_needed, time_needed)
