
# Read input
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Create a dictionary to store the positions of each student in the initial order
positions = {}
for i in range(N):
    positions[initial_order[i]] = i

# Initialize variables
inspections = 0
new_positions = []

# Iterate through the names list
for name in names_list:
    # Calculate the distance between the current position and the desired position
    distance = positions[name] - inspections
    if distance < 0:
        distance += N
    new_positions.append(distance)
    inspections += distance

# Output the result
print(inspections)
print(*new_positions)
