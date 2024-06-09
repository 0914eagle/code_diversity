
# Read input values
N, M, K = map(int, input().split())
buildings = [0] * M
students = [int(input()) for _ in range(N)]

# Initialize variables
total_noise = 0
remaining_moves = K

# Calculate noise level
for student in students:
    buildings[student-1] += 1
    total_noise += buildings[student-1]
    if remaining_moves > 0:
        max_noise_building = max(buildings)
        total_noise -= max_noise_building
        buildings[buildings.index(max_noise_building)] = 0
        remaining_moves -= 1

# Output the minimal possible total noise level
print(total_noise)
