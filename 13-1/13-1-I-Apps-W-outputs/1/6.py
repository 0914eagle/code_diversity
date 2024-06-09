
n, s, t = map(int, input().split())
p = list(map(int, input().split()))

# Check if the marble can move from position s to position t
if s == t:
    print(0)
    exit()

# Initialize a dictionary to keep track of the positions of the marble
positions = {s: 1}

# Iterate through the shuffling operations
for i in range(n - 1):
    # Get the current position of the marble
    current_position = positions[s]
    
    # Check if the marble has reached its final position
    if current_position == t:
        print(i + 1)
        exit()
    
    # Update the dictionary with the new position of the marble
    positions[s] = p[current_position - 1]

# If the marble has not reached its final position, it is impossible to move it
print(-1)

