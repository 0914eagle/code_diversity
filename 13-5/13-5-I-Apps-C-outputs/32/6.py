
def longest_path(N, M, roads):
    # Initialize a dictionary to store the length of the longest path from each city
    longest_paths = {i: 0 for i in range(1, N + 1)}
    longest_paths[1] = 1

    # Iterate through each road
    for road in roads:
        # Get the two cities connected by the road
        city1, city2 = road

        # If the length of the longest path from city1 is greater than the length of the longest path from city2,
        # then update the length of the longest path from city2 to be the length of the longest path from city1 plus 1
        if longest_paths[city1] > longest_paths[city2]:
            longest_paths[city2] = longest_paths[city1] + 1

        # If the length of the longest path from city2 is greater than the length of the longest path from city1,
        # then update the length of the longest path from city1 to be the length of the longest path from city2 plus 1
        elif longest_paths[city2] > longest_paths[city1]:
            longest_paths[city1] = longest_paths[city2] + 1

    # Return the longest path from city 1
    return longest_paths[1]

