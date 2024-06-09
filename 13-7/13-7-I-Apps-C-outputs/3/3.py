
def hopper_exploration(array, d, m):
    # Initialize a set to keep track of visited indices
    visited = set()
    # Initialize a variable to keep track of the longest exploration sequence
    longest = 0
    # Loop through each element in the array
    for i in range(len(array)):
        # If the element has not been visited before, visit it and explore its neighbors
        if i not in visited:
            visited.add(i)
            # Find the neighbors of the current element that are within the given distance d and have a difference in value less than or equal to m
            neighbors = [j for j in range(i-d, i+d+1) if j >= 0 and j < len(array) and abs(array[i] - array[j]) <= m and j not in visited]
            # Recursively explore the neighbors and update the longest exploration sequence
            longest = max(longest, 1 + hopper_exploration(array, d, m, visited | set(neighbors)))
    return longest

