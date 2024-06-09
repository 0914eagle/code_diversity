
def max_cuts(sequence, budget):
    # Initialize variables
    n = len(sequence)
    odd_count = 0
    even_count = 0
    cost = 0
    cuts = 0

    # Count the number of odd and even numbers in the sequence
    for i in range(n):
        if sequence[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Loop through the sequence and check if it is possible to make a cut
    for i in range(n - 1):
        # Check if the current element and the next element have the same parity
        if sequence[i] % 2 == sequence[i + 1] % 2:
            # If the cost of the cut is less than or equal to the budget, make the cut
            if cost + abs(sequence[i] - sequence[i + 1]) <= budget:
                cost += abs(sequence[i] - sequence[i + 1])
                cuts += 1
        # If the current element and the next element have different parity, check if the cost of the cut is less than the budget
        else:
            # If the cost of the cut is less than the budget, make the cut
            if cost + abs(sequence[i] - sequence[i + 1]) <= budget:
                cost += abs(sequence[i] - sequence[i + 1])
                cuts += 1

    # Return the maximum number of cuts possible with the given budget
    return cuts

