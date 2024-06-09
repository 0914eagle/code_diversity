
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

    # Calculate the maximum number of cuts that can be made
    for i in range(n - 1):
        if sequence[i] % 2 == 0 and sequence[i + 1] % 2 == 0:
            cost += 1
        elif sequence[i] % 2 == 1 and sequence[i + 1] % 2 == 1:
            cost += 1
        else:
            cost += 2
        if cost <= budget:
            cuts += 1

    # Return the maximum number of cuts
    return cuts

