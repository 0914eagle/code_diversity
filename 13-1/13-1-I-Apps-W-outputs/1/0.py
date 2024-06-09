
n, s, t = map(int, input().split())
p = list(map(int, input().split()))

# Check if the marble can move from position s to position t
if s == t:
    print(0)
    exit()

# Initialize a dictionary to keep track of the glasses' positions
positions = {i: i for i in range(1, n + 1)}

# Initialize a set to keep track of the glasses that have been shuffled
shuffled = set()

# Initialize a variable to keep track of the number of shuffling operations
operations = 0

# Loop through the shuffling operations
for i in range(n):
    # Check if the current glass has been shuffled
    if i not in shuffled:
        # Get the position of the current glass
        current_position = positions[i]
        
        # Check if the current glass is the one that the marble is on
        if current_position == s:
            # Set the marble's position to the position of the current glass
            marble_position = current_position
        
        # Check if the current glass is the one that the marble is moving to
        if current_position == t:
            # Print the minimum number of shuffling operations needed to get the marble to position t
            print(operations)
            exit()
        
        # Shuffle the current glass
        shuffled.add(i)
        positions[i] = p[i]
        operations += 1

# If the marble cannot move from position s to position t, print -1
print(-1)

