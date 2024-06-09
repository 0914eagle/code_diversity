
def calculate_probability(Tg, Ty, Tr, n, observations, tq, cq):
    total_green_time = Tg
    total_yellow_time = Ty
    total_red_time = Tr
    total_cycle_time = Tg + Ty + Tr

    green_count = 0
    total_count = 0

    for i in range(n):
        t, color = observations[i]
        cycle_start_time = t - (t % total_cycle_time)
        cycle_end_time = cycle_start_time + total_cycle_time

        while t < cycle_end_time:
            if color == 'green':
                if t <= tq < t + Tg:
                    green_count += 1
                total_count += 1
            t += total_cycle_time

    if total_count == 0:
        return 0

    probability = green_count / total_count if cq == 'green' else 1 - (green_count / total_count)
    return round(probability, 3)

# Input parsing
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))
tq, cq = input().split()

# Calculate and output the probability
result = calculate_probability(Tg, Ty, Tr, n, observations, int(tq), cq)
print(result)
