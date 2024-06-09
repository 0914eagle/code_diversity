
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
        # If the road is not already in the dictionary, add it
        if road not in road_dict:
            road_dict[road] = 1
        # If the road is already in the dictionary, increment the count
        else:
            road_dict[road] += 1
    # Initialize a list to store the longest Fibonacci Tour
    longest_tour = []
    # Loop through each mansion height
    for height in mansion_heights:
        # If the mansion height is not already in the longest tour, add it
        if height not in longest_tour:
            longest_tour.append(height)
        # If the mansion height is already in the longest tour, check if there is a road between the current mansion and the previous mansion
        else:
            # Get the index of the mansion height in the longest tour
            index = longest_tour.index(height)
            # If there is a road between the current mansion and the previous mansion, add the current mansion to the longest tour
            if (longest_tour[index - 1], height) in road_dict:
                longest_tour.append(height)
    # Return the length of the longest Fibonacci Tour
    return len(longest_tour)

