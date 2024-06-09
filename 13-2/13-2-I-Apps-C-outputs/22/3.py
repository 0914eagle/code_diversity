
import sys
input = sys.stdin.read()
n, m = map(int, input.split('\n')[0].split())
neighbors = [set() for _ in range(n)]
for i in range(m):
    u, v = map(int, input.split('\n')[i+1].split())
    neighbors[u].add(v)
    neighbors[v].add(u)
s, t = map(int, input.split('\n')[-1].split())

# Initialize the probability of meeting at each station
prob = [0] * n
prob[s] = 1
prob[t] = 1

# Loop until the probability of meeting at each station is the same
while True:
    new_prob = [0] * n
    for i in range(n):
        for j in neighbors[i]:
            new_prob[i] += prob[j] / len(neighbors[i])
    if new_prob == prob:
        break
    prob = new_prob

# Calculate the expected time of meeting
expected_time = 0
for i in range(n):
    expected_time += prob[i] * i
expected_time /= sum(prob)

print(expected_time)

