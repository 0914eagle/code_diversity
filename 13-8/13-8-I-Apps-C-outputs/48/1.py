
def solve(n, distances):
    # Initialize the subsets A and B
    A, B = set(), set()
    # Initialize the minimum sum of disparities
    min_sum = float('inf')
    # Iterate over all possible subsets of the shipments
    for i in range(1 << n):
        # Convert the binary representation of i to a subset of shipments
        subset = {j for j in range(n) if i & (1 << j)}
        # Calculate the disparity of the subset
        disparity = max([distances[i][j] for i in subset for j in subset if i != j])
        # If the sum of the disparities is smaller than the current minimum, update the minimum sum and the subsets A and B
        if sum(disparity, A, B) < min_sum:
            min_sum = sum(disparity, A, B)
            A, B = subset, subset - A
    # Return the minimum sum of disparities
    return min_sum

