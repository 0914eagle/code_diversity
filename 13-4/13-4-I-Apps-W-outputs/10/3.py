
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
            continue
        # Calculate the cost of the cut
        cost += abs(sequence[i] - sequence[i + 1])
        # Check if the cost is within budget
        if cost > budget:
            break
        # Increment the number of cuts
        cuts += 1

    return cuts

