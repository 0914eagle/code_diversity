
def calculate_probability(T_g, T_y, T_r, n, observations, t_q, c_q):
    total_time = T_g + T_y + T_r
    green_times = []
    
    for i in range(n):
        t, c = observations[i]
        if c == 'green':
            green_times.append(t)
    
    green_count = 0
    for time in green_times:
        cycle_start = time % total_time
        if c_q == 'green':
            if cycle_start <= t_q < cycle_start + T_g:
                green_count += 1
        elif c_q == 'yellow':
            if cycle_start + T_g <= t_q < cycle_start + T_g + T_y:
                green_count += 1
        elif c_q == 'red':
            if cycle_start + T_g + T_y <= t_q < cycle_start + T_g + T_y + T_r:
                green_count += 1
    
    probability = green_count / n
    return probability

# Input
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
