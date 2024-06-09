
def solve(n, systems, e, links):
    # Initialize the minimum UW distance to a large value
    min_distance = 1000000
    # Loop through all possible pairs of systems
    for i in range(n):
        for j in range(i+1, n):
            # If the systems are of different types, calculate the UW distance
            if systems[i][1] != systems[j][1]:
                distance = calculate_distance(systems[i][0], systems[j][0], links)
                # If the distance is less than the minimum distance, update the minimum distance
                if distance < min_distance:
                    min_distance = distance
    # Return the minimum UW distance
    return min_distance

def calculate_distance(system1, system2, links):
    # Initialize the UW distance to 0
    distance = 0
    # If the systems are directly linked, return the distance between them
    if (system1, system2) in links or (system2, system1) in links:
        return distance
    # Otherwise, calculate the distance by hopping through intermediary systems
    else:
        # Loop through all systems directly linked to system1
        for i in links:
            # If the system is directly linked to system2, return the distance between them
            if i[1] == system2:
                return distance
            # Otherwise, calculate the distance to the next system and add it to the total distance
            else:
                distance += calculate_distance(i[1], system2, links)
        # Return the total distance
        return distance

# Test the function with the sample input
n = 9
systems = [(377, 'a'), (455, 'h'), (180, 'a'), (211, 'a'), (134, 'a'), (46, 'h'), (111, 'h'), (213, 'h'), (17, 'a')]
e = 15
links = [(1, 2), (1, 4), (1, 6), (2, 3), (2, 4), (2, 5), (3, 5), (4, 6), (4, 7), (4, 9), (5, 7), (5, 8), (6, 9), (7, 9), (7, 8)]
print(solve(n, systems, e, links))

