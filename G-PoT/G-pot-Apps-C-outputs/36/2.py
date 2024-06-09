
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_soda = sum(a)
sorted_bottles = sorted(zip(a, b), key=lambda x: x[1])

current_soda = 0
bottles_needed = 0
time_needed = 0

for soda, volume in sorted_bottles:
    if current_soda >= total_soda - current_soda:
        break
    current_soda += soda
    bottles_needed += 1
    time_needed += soda

print(bottles_needed, time_needed)
