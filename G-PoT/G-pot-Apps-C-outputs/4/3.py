
# Read input
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Initialize variables
inspections = 0
positions_to_go_back = []

# Create a dictionary to store the positions of each student in the initial order
positions_dict = {initial_order[i]: i for i in range(N)}

# Iterate through the names list
for name in names_list:
    # Calculate the position of the student in the initial order
    position = positions_dict[name]
    
    # Calculate the number of positions the student needs to go back
    go_back = position - inspections
    
    # Update the inspections count
    inspections += 1
    
    # Add the go back position to the list
    positions_to_go_back.append(go_back)

# Output the result
print(inspections)
print(*positions_to_go_back)
