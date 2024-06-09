
import sys
import math

def solve(n, m, passages):
    # Initialize the expected number of passages as 0
    E = 0
    
    # Loop through each passage
    for i in range(m):
        # Get the current passage
        s, t = passages[i]
        
        # If the passage is from Room 1 to Room 2, block it
        if s == 1 and t == 2:
            continue
        
        # Add the probability of taking this passage to the expected number of passages
        E += (t - s) / n
    
    # Return the expected number of passages
    return E

n, m = map(int, input().split())
passages = []

# Loop through each passage
for i in range(m):
    # Get the current passage
    s, t = map(int, input().split())
    
    # Add the passage to the list of passages
    passages.append((s, t))

# Call the solve function and print the result
print(solve(n, m, passages))

