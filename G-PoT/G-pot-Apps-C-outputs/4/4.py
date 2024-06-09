
# Read input
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Initialize variables
inspections = 0
positions = []

# Create a dictionary to store the positions of each student in the initial order
positions_dict = {student: i for i, student in enumerate(initial_order)}

# Iterate through the names list
for name in names_list:
    # Calculate the position of the student in the initial order
    position = positions_dict[name]
    
    # Calculate the number of inspections needed to reach the student
    inspections_needed = position - inspections
    
    # Update the inspections count
    inspections += inspections_needed
    
    # Update the positions list
    positions.extend([position + 1] * inspections_needed)
    
    # Update the position of the student in the initial order
    positions_dict[name] = inspections - 1

# Print the output
print(inspections)
print(*positions)
