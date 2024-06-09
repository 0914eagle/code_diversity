
def get_fibonacci_tour(n, m, heights, roads):
    # Initialize a list to store the Fibonacci sequence
    fibonacci_seq = [1, 1]
    # Loop until the length of the Fibonacci sequence is equal to n
    while len(fibonacci_seq) < n:
        # Get the last two numbers in the Fibonacci sequence
        a, b = fibonacci_seq[-1], fibonacci_seq[-2]
        # Calculate the next number in the Fibonacci sequence
        fibonacci_seq.append(a + b)
    # Initialize a dictionary to store the mansion heights and the mansion indices
    mansion_heights = {i: heights[i-1] for i in range(1, n+1)}
    # Initialize a list to store the mansion indices in the Fibonacci sequence
    fibonacci_indices = []
    # Loop through the Fibonacci sequence
    for i in range(len(fibonacci_seq)):
        # Get the current Fibonacci number
        fibonacci_number = fibonacci_seq[i]
        # Loop through the mansion heights
        for mansion_index, mansion_height in mansion_heights.items():
            # Check if the mansion height is equal to the current Fibonacci number
            if mansion_height == fibonacci_number:
                # Add the mansion index to the list of Fibonacci indices
                fibonacci_indices.append(mansion_index)
                # Break out of the loop
                break
    # Initialize a list to store the mansion indices in the Fibonacci tour
    tour = []
    # Loop through the Fibonacci indices
    for i in range(len(fibonacci_indices)):
        # Get the current Fibonacci index
        current_index = fibonacci_indices[i]
        # Check if the current index is not in the tour
        if current_index not in tour:
            # Add the current index to the tour
            tour.append(current_index)
            # Loop through the roads
            for road in roads:
                # Check if the current index is equal to the first index in the road
                if current_index == road[0]:
                    # Get the second index in the road
                    next_index = road[1]
                    # Check if the next index is not in the tour
                    if next_index not in tour:
                        # Add the next index to the tour
                        tour.append(next_index)
                        # Break out of the loop
                        break
    # Return the length of the tour
    return len(tour)

n, m = map(int, input().split())
heights = list(map(int, input().split()))
roads = []
for i in range(m):
    a, b = map(int, input().split())
    roads.append([a, b])
print(get_fibonacci_tour(n, m, heights, roads))

