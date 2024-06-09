
# Read input
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))
tq, cq = input().split()
tq = int(tq)

# Calculate the total cycle time
cycle_time = Tg + Ty + Tr

# Initialize variables
total_possible_times = 0
green_times = 0

# Iterate through observations
for i in range(n):
    t, color = observations[i]
    next_t, next_color = observations[(i + 1) % n]

    # Calculate the time difference between observations
    time_diff = next_t - t
    if time_diff < 0:
        time_diff += cycle_time

    # Check if the lights were green during this time period
    if color == 'red' and next_color == 'green':
        total_possible_times += 1
        if t <= tq < next_t:
            green_times += 1
    elif color == 'yellow' and next_color == 'green':
        total_possible_times += 1
        if t <= tq < next_t:
            green_times += 1
    elif color == 'green' and next_color == 'red':
        total_possible_times += 1
        if t <= tq < next_t:
            green_times += 1

# Calculate the probability
if total_possible_times == 0:
    probability = 0
else:
    probability = green_times / total_possible_times

print(probability)
