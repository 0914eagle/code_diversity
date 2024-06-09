
import sys
input = sys.stdin.read()
n, m = map(int, input.split('\n')[0].split())
neighbors = [set(map(int, input.split('\n')[i].split())) for i in range(1, m+1)]
s, t = map(int, input.split('\n')[-1].split())

# Initialize the probability of meeting at each station
probability = [0] * n
probability[s] = 1
probability[t] = 1

# Loop through each minute
for i in range(1, n):
    # Find the neighbors of the current stations
    neighbor_s = neighbors[s]
    neighbor_t = neighbors[t]
    
    # Update the probability of meeting at each station
    for j in range(n):
        if j in neighbor_s:
            probability[j] += probability[s] / len(neighbor_s)
        if j in neighbor_t:
            probability[j] += probability[t] / len(neighbor_t)
    
    # Update the current stations
    s = (s + 1) % n
    t = (t + 1) % n

# Find the station with the highest probability of meeting
max_prob = max(probability)
meeting_station = probability.index(max_prob)

# Output the expected time of meeting
print(meeting_station)

