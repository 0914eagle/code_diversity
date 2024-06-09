
from collections import defaultdict

def calculate_probability(Tg, Ty, Tr, n, observations, tq, cq):
    colors = {'green': 0, 'yellow': 1, 'red': 2}
    cycle_length = Tg + Ty + Tr
    counts = defaultdict(int)
    
    for i in range(n-1):
        t, color = observations[i]
        next_t, next_color = observations[i+1]
        duration = next_t - t
        counts[(colors[color], colors[next_color])] += duration
    
    t_last, color_last = observations[-1]
    counts[(colors[color_last], colors[observations[0][1]])] += tq - t_last
    
    total_counts = sum(counts.values())
    target_color = colors[cq]
    target_count = 0
    
    for key, value in counts.items():
        if key[1] == target_color:
            target_count += value
    
    probability = target_count / total_counts
    return probability

# Input parsing
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))
tq, cq = input().split()
tq = int(tq)

# Calculate probability
probability = calculate_probability(Tg, Ty, Tr, n, observations, tq, cq)
print(probability)
