
def solve(n, s, t, q, hills, springs, towns):
    # Calculate the total length of all aqueducts
    total_length = 0
    for i in range(t):
        # Find the spring and town for each town
        spring = springs[i]
        town = towns[i]
        # Calculate the distance between the spring and town
        distance = abs(hills[spring][0] - hills[town][0]) + abs(hills[spring][1] - hills[town][1])
        # Add the distance to the total length
        total_length += distance
    
    # Return the total length
    return total_length

