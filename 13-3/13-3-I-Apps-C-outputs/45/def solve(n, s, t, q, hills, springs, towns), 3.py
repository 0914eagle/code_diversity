
def solve(n, s, t, q, hills, springs, towns):
    # Calculate the total length of all aqueducts
    total_length = 0
    for i in range(t):
        # Find the spring and town for each town
        spring = springs[i]
        town = towns[i]
        # Calculate the distance between the spring and town
        distance = calculate_distance(hills, spring, town)
        # Add the distance to the total length
        total_length += distance
    
    # Return the total length
    return total_length

def calculate_distance(hills, spring, town):
    # Find the coordinates of the spring and town
    spring_coords = hills[spring - 1]
    town_coords = hills[town - 1]
    # Calculate the distance between the spring and town
    distance = ((spring_coords[0] - town_coords[0]) ** 2 + (spring_coords[1] - town_coords[1]) ** 2) ** 0.5
    # Return the distance
    return distance

# Test the function with the sample input
n = 6
s = 2
t = 2
q = 8
hills = [(0, 0, 6), (3, 4, 7), (0, 8, 8), (6, 8, 8), (6, 0, 6), (6, 4, 8)]
springs = [3, 1]
towns = [5, 4]
print(solve(n, s, t, q, hills, springs, towns))

