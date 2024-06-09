
def get_longest_path(N, M, roads):
    # Initialize a dictionary to store the length of the longest path from each city
    longest_path_from_city = {}
    for city in range(1, N+1):
        longest_path_from_city[city] = 0

    # Loop through each road
    for road in roads:
        # Get the two cities connected by the road
        city1, city2 = road

        # If the length of the longest path from city1 is greater than the length of the longest path from city2,
        # then update the length of the longest path from city2 to be the length of the longest path from city1 plus 1
        if longest_path_from_city[city1] > longest_path_from_city[city2]:
            longest_path_from_city[city2] = longest_path_from_city[city1] + 1

    # Return the length of the longest path from city 1
    return longest_path_from_city[1]

