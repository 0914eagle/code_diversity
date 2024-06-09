
def fibonacci_tour(n, m, heights, roads):
    # Initialize a list to store the Fibonacci sequence
    fib = [1, 1]
    # Loop until the next Fibonacci number is greater than the number of mansions
    while fib[-1] <= n:
        # Add the next Fibonacci number to the list
        fib.append(fib[-1] + fib[-2])
    # Initialize a list to store the mansion heights in the Fibonacci sequence
    fib_heights = []
    # Loop through the Fibonacci sequence
    for i in range(len(fib)):
        # If the current Fibonacci number is less than or equal to the number of mansions, add the corresponding mansion height to the list
        if fib[i] <= n:
            fib_heights.append(heights[fib[i] - 1])
    # Initialize a dictionary to store the mansion heights and their indices
    mansion_heights = {height: i for i, height in enumerate(heights)}
    # Initialize a list to store the mansion indices in the Fibonacci sequence
    fib_indices = []
    # Loop through the Fibonacci sequence
    for i in range(len(fib)):
        # If the current Fibonacci number is less than or equal to the number of mansions, add the corresponding mansion index to the list
        if fib[i] <= n:
            fib_indices.append(mansion_heights[fib_heights[i]])
    # Initialize a list to store the mansion indices in the Fibonacci sequence that are connected by a road
    connected_indices = []
    # Loop through the roads
    for road in roads:
        # If the current road is connected by a road, add the corresponding mansion indices to the list
        if road[0] in fib_indices and road[1] in fib_indices:
            connected_indices.append(road)
    # Initialize a list to store the longest Fibonacci Tour
    longest_tour = []
    # Loop through the mansion indices in the Fibonacci sequence
    for i in range(len(fib_indices)):
        # If the current mansion index is connected by a road to the previous mansion index, add the current mansion index to the list
        if i > 0 and connected_indices[i - 1][1] == fib_indices[i]:
            longest_tour.append(fib_indices[i])
        # If the current mansion index is not connected by a road to the previous mansion index, start a new tour
        else:
            longest_tour = [fib_indices[i]]
    # Return the length of the longest Fibonacci Tour
    return len(longest_tour)

