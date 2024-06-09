
# Read input
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Initialize variables
inspections = 0
positions_to_go_back = []

# Create a dictionary to store the positions of each name in the initial order
positions_dict = {name: i for i, name in enumerate(initial_order)}

# Iterate through the names in the list
for name in names_list:
    if positions_dict[name] == 0:
        positions_to_go_back.append(name)
    else:
        positions_to_go_back.append(name)
        inspections += 1
        new_position = positions_dict[name]
        initial_order.pop(new_position)
        initial_order.insert(0, name)
        positions_dict = {name: i for i, name in enumerate(initial_order)}

# Output results
print(inspections)
print(' '.join(map(str, positions_to_go_back)))
