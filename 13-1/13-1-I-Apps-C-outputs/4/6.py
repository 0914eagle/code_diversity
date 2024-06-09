
n, m, k = map(int, input().split())
p = list(map(int, input().split()))

# Initialize a list to store the positions of the special items
special_positions = []

# Loop through the list of special items and add their positions to the list
for i in range(m):
    special_positions.append(p[i])

# Initialize a variable to store the number of operations
operations = 0

# Loop through the list of special items and discard them one by one
for i in range(m):
    # Find the page that contains the special item
    page = special_positions[i] // k
    
    # Discard the special item
    special_positions[i] = -1
    
    # Update the positions of the items below the special item
    for j in range(i+1, m):
        if special_positions[j] > special_positions[i]:
            special_positions[j] -= 1
    
    # Increment the number of operations
    operations += 1

# Print the number of operations
print(operations)

