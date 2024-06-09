
# Read input values
N, M, K = map(int, input().split())
buildings = list(map(int, input().split()))

# Initialize a list to store the number of students in each building
students_in_building = [0] * M

# Initialize a list to store the total noise level for each building
noise_levels = [0] * M

# Initialize a variable to store the total noise level
total_noise = 0

# Iterate through each day
for building in buildings:
    building -= 1  # Adjust building index to start from 0
    students_in_building[building] += 1
    noise_levels[building] += students_in_building[building]
    total_noise += noise_levels[building]

    # Check if we can empty a building
    if K > 0:
        empty_building = max(range(M), key=lambda x: noise_levels[x])
        if empty_building != building:
            K -= 1
            total_noise -= noise_levels[empty_building]
            noise_levels[empty_building] = 0
            students_in_building[building] += students_in_building[empty_building]
            students_in_building[empty_building] = 0

print(total_noise)
