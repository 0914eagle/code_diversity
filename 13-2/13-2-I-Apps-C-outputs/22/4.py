
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
for i in range(1, 60):
    # Update the probability of meeting at each station
    for u in range(n):
        if u != s and u != t:
            probability[u] += probability[s] * (1 - probability[u]) / (n - 2)
            probability[u] += probability[t] * (1 - probability[u]) / (n - 2)
    
    # Update the probability of meeting at the meeting spot of each station
    for u in range(n):
        for v in neighbors[u]:
            if u != s and u != t and v != s and v != t:
                probability[u] += probability[s] * probability[v] / (n - 2)
                probability[u] += probability[t] * probability[v] / (n - 2)
    
    # Check if Alice and Bob will meet
    if probability[s] > 0 and probability[t] > 0:
        break

# Print the expected time of meeting
print(i)

