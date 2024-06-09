
def solve(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    # Initialize the left and right indices for each splitter
    l, r = [], []
    # While the global input is not distributed in the desired ratio
    while c/(c+d) != a/(a+b):
        # Calculate the ratio of the global input that needs to be sent to the left output
        left_ratio = c/(c+d)
        # Calculate the ratio of the global input that needs to be sent to the right output
        right_ratio = d/(c+d)
        # Calculate the ratio of the input that needs to be sent to the left output for each splitter
        left_splitter_ratio = a/(a+b)
        # Calculate the ratio of the input that needs to be sent to the right output for each splitter
        right_splitter_ratio = b/(a+b)
        # Calculate the number of splitters needed to achieve the desired ratio
        num_splitters = int(left_ratio / left_splitter_ratio) + int(right_ratio / right_splitter_ratio)
        # Add the splitters to the list
        l += [-1] * num_splitters
        r += [-2] * num_splitters
        # Update the number of splitters
        n += num_splitters
        # Update the global input ratio
        c = c - left_ratio * num_splitters
        d = d - right_ratio * num_splitters
    # Return the number of splitters and the left and right indices for each splitter
    return n, l, r

