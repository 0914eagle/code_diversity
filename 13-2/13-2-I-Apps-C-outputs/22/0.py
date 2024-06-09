
import sys
input = sys.stdin.read()
n, m = map(int, input.split('\n')[0].split())
neighbors = [set(map(int, input.split('\n')[i].split())) for i in range(1, m+1)]
s, t = map(int, input.split('\n')[-1].split())

# Initialize the probability of meeting at each station
prob = [0] * n
prob[s] = 1
prob[t] = 1

# Loop until the probability of meeting at each station is the same
while True:
    # Calculate the probability of meeting at each neighboring station
    for i in range(n):
        if i not in neighbors[i]:
            continue
        for j in neighbors[i]:
            prob[j] += prob[i] / len(neighbors[i])
    
    # Check if the probability of meeting at each station is the same
    if all(prob[i] == prob[-1] for i in range(n)):
        break

# Calculate the expected time of meeting
expected_time = 0
for i in range(n):
    expected_time += prob[i] * (i + 1)

print(expected_time)

