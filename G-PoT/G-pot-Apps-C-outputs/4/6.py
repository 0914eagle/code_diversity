
# Read input
N, M = map(int, input().split())
attendance_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Initialize variables
inspections = 0
positions = []

# Create a dictionary to store the positions of each student in the initial order
positions_dict = {student: i for i, student in enumerate(initial_order)}

# Iterate through the attendance list
for student in attendance_list:
    # Calculate the number of positions to move the student back
    move_back = positions_dict[student] - inspections
    
    # Update the inspections count and append the move back position to the list
    inspections += max(0, move_back)
    positions.append(max(0, move_back) + 1)

# Output the results
print(inspections)
print(" ".join(map(str, positions)))
