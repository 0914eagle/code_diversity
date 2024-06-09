
# Read input
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))
t_q, c_q = input().split()
t_q = int(t_q)

# Calculate the total cycle time
cycle_time = Tg + Ty + Tr

# Initialize variables
total_possible_cycles = 0
green_cycles = 0

# Iterate through observations to find possible cycles
for i in range(n):
    t, color = observations[i]
    if color == "green":
        start_time = t - Tg
        while start_time < t_q:
            start_time += cycle_time
        if start_time == t_q:
            green_cycles += 1
        total_possible_cycles += 1

# Calculate probability
if total_possible_cycles == 0:
    probability = 0
else:
    probability = green_cycles / total_possible_cycles

print(probability)
