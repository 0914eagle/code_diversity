
def calculate_probability(T_g, T_y, T_r, n, observations, t_q, c_q):
    total_time = T_g + T_y + T_r
    count_green = 0
    count_total = 0
    
    for i in range(n):
        t, c = observations[i]
        cycle_start = t - (t % total_time)
        
        if c == 'green':
            count_total += 1
            if (cycle_start + T_g) % total_time <= t % total_time:
                count_green += 1
        elif c == 'yellow':
            if (cycle_start + T_g) % total_time <= t % total_time < (cycle_start + T_g + T_y) % total_time:
                count_total += 1
                if (cycle_start + T_g) % total_time <= t_q % total_time < (cycle_start + T_g + T_y) % total_time:
                    count_green += 1
        elif c == 'red':
            if (cycle_start + T_g + T_y) % total_time <= t % total_time < (cycle_start + T_g + T_y + T_r) % total_time:
                count_total += 1
                if (cycle_start + T_g + T_y) % total_time <= t_q % total_time < (cycle_start + T_g + T_y + T_r) % total_time:
                    count_green += 1
    
    if count_total == 0:
        return 0
    else:
        return count_green / count_total

# Input parsing
T_g, T_y, T_r = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, c = input().split()
    observations.append((int(t), c))
t_q, c_q = input().split()

# Calculate probability
probability = calculate_probability(T_g, T_y, T_r, n, observations, int(t_q), c_q)
print(probability)
