
def get_fibonacci_tour(n, m, heights, roads):
    # Initialize a list to store the Fibonacci sequence
    fibonacci_seq = [1, 1]
    # Loop until the length of the Fibonacci sequence is equal to n
    while len(fibonacci_seq) < n:
        # Get the last two numbers in the Fibonacci sequence
        a, b = fibonacci_seq[-1], fibonacci_seq[-2]
        # Calculate the next number in the Fibonacci sequence
        fibonacci_seq.append(a + b)
    # Initialize a list to store the mansion heights
    mansion_heights = []
    # Loop through each mansion height
    for height in heights:
        # If the mansion height is in the Fibonacci sequence, add it to the list of mansion heights
        if height in fibonacci_seq:
            mansion_heights.append(height)
    # Initialize a dictionary to store the roads between mansions
    road_dict = {}
    # Loop through each road
    for road in roads:
        # Get the two mansions connected by the road
        a, b = road[0], road[1]
        # If the mansions are not already in the dictionary, add them with an empty list of roads
        if a not in road_dict:
            road_dict[a] = []
        if b not in road_dict:
            road_dict[b] = []
        # Add the road to the list of roads for both mansions
        road_dict[a].append(b)
        road_dict[b].append(a)
    # Initialize a list to store the longest Fibonacci Tour
    longest_tour = []
    # Loop through each mansion height
    for height in mansion_heights:
        # If the mansion height is not already in the longest tour, add it to the tour
        if height not in longest_tour:
            longest_tour.append(height)
            # Get the list of roads for the mansion
            roads = road_dict[height]
            # Loop through each road
            for road in roads:
                # If the road is not already in the longest tour, add it to the tour
                if road not in longest_tour:
                    longest_tour.append(road)
    # Return the length of the longest Fibonacci Tour
    return len(longest_tour)

n, m = map(int, input().split())
heights = list(map(int, input().split()))
roads = []
for i in range(m):
    a, b = map(int, input().split())
    roads.append([a, b])
print(get_fibonacci_tour(n, m, heights, roads))

