
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    left = [-1] * 200
    right = [-1] * 200
    # Set the global input to be connected to splitter 0
    left[0] = -2
    right[0] = -1
    # Loop until we have reached the desired ratio
    while c > 0 or d > 0:
        # If the current ratio is not the desired ratio, insert a new splitter
        if a != c or b != d:
            # Find the splitter with the largest ratio that is less than the desired ratio
            max_ratio = 0
            max_index = -1
            for i in range(n):
                if left[i] != -1 and right[i] != -1 and a * d > c * b:
                    ratio = a * d / (c * b)
                    if ratio > max_ratio:
                        max_ratio = ratio
                        max_index = i
            # If no suitable splitter is found, return -1
            if max_index == -1:
                return -1
            # Insert the new splitter and update the left and right indices
            n += 1
            left[n] = left[max_index]
            right[n] = right[max_index]
            left[max_index] = n
            right[max_index] = n
        # Update the current ratio
        a, b = a + c, b + d
        c, d = 0, 0
    # Return the number of splitters and the left and right indices
    return n, left, right

