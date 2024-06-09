
import sys
input = sys.stdin.read()
n, m = map(int, input.split('\n')[0].split())
neighbors = [set() for _ in range(n)]
for i in range(m):
    u, v = map(int, input.split('\n')[i + 1].split())
    neighbors[u].add(v)
    neighbors[v].add(u)
s, t = map(int, input.split('\n')[-1].split())

# Initialize the probability of meeting at each station
prob = [0] * n
prob[s] = 1
prob[t] = 1

# Iterate through each minute
for i in range(1, n * n):
    # Find the current station of Alice and Bob
    current_s = (s + i) % n
    current_t = (t + i) % n
    
    # If they are at the same station, they meet
    if current_s == current_t:
        print(i)
        break
    
    # Otherwise, they take a train to a neighboring station
    neighbors_s = neighbors[current_s]
    neighbors_t = neighbors[current_t]
    for neighbor_s in neighbors_s:
        for neighbor_t in neighbors_t:
            prob[neighbor_s] += prob[current_s] / len(neighbors_s)
            prob[neighbor_t] += prob[current_t] / len(neighbors_t)
    
    # Reset the probability of meeting at the current station
    prob[current_s] = 0
    prob[current_t] = 0

# If they never meet, print "never meet"
else:
    print("never meet")

