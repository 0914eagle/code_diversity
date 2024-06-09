
# Read input
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Initialize variables
inspections = 0
positions_to_go_back = []

# Create a dictionary to store the positions of each student in the initial order
positions_dict = {student: pos for pos, student in enumerate(initial_order, start=1)}

# Iterate through the names list
for name in names_list:
    # Get the position of the student in the initial order
    position = positions_dict[name]
    
    # Calculate the number of inspections needed to reach this student
    inspections_needed = position - inspections
    
    # Update the total number of inspections
    inspections += inspections_needed
    
    # Add the number of inspections needed to the positions_to_go_back list
    positions_to_go_back.append(inspections_needed)
    
    # Update the position of the student in the positions_dict
    positions_dict[name] = inspections

# Output the results
print(inspections)
print(' '.join(map(str, positions_to_go_back)))
