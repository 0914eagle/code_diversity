
def calculate_probability(T_g, T_y, T_r, n, observations, t_q, c_q):
    total_time = T_g + T_y + T_r
    green_times = []
    for i in range(n):
        t, color = observations[i]
        if color == 'green':
            green_times.append(t)
    
    count = 0
    for green_time in green_times:
        cycle_start = green_time - T_g
        while cycle_start <= t_q:
            if cycle_start <= t_q < cycle_start + T_g:
                if c_q == 'green':
                    count += 1
                break
            cycle_start += total_time
    
    probability = count / len(green_times)
    return probability

# Input
T_g, T_y, T_r = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))
t_q, c_q = input().split()

# Calculate probability
probability = calculate_probability(T_g, T_y, T_r, n, observations, int(t_q), c_q)
print(probability)
