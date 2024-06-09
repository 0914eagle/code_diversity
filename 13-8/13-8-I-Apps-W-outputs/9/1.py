
def max_cuts(sequence, budget):
    # Initialize variables
    n = len(sequence)
    odd_count = 0
    even_count = 0
    cost = 0
    cuts = 0

    # Iterate through the sequence
    for i in range(n):
        # Check if the current element is odd or even
        if sequence[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        # Check if the current element is the last one in the sequence
        if i == n - 1:
            # If the number of odd and even elements is not equal, return 0
            if odd_count != even_count:
                return 0
            # Otherwise, return the number of cuts
            return cuts

        # Check if the current element is the first one in the sequence
        if i == 0:
            continue

        # Calculate the cost of the current cut
        cost += abs(sequence[i] - sequence[i - 1])

        # Check if the current cost is less than or equal to the budget
        if cost <= budget:
            # Increment the number of cuts
            cuts += 1
        else:
            # If the current cost is greater than the budget, return 0
            return 0

    # If the function reaches this point, return the number of cuts
    return cuts

