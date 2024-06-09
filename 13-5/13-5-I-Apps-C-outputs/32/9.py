
def longest_race_path(N, M, roads):
    # Initialize a dictionary to store the length of the longest path from each city
    longest_paths = {i: 0 for i in range(1, N + 1)}
    longest_paths[1] = 1

    # Iterate through each road
    for road in roads:
        city1, city2 = road
        if longest_paths[city1] > longest_paths[city2]:
            longest_paths[city2] = longest_paths[city1]
        else:
            longest_paths[city1] = longest_paths[city2]

    # Return the longest path from city 1
    return longest_paths[1]

