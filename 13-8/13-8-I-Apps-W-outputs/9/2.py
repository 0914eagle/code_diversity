
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
        if odd_count == even_count:
            break
        if sequence[i] % 2 == 0 and sequence[i + 1] % 2 == 1:
            odd_count += 1
            even_count -= 1
            cost += 1
            cuts += 1
        elif sequence[i] % 2 == 1 and sequence[i + 1] % 2 == 0:
            odd_count -= 1
            even_count += 1
            cost += 1
            cuts += 1

    # Check if the total cost is less than or equal to the budget
    if cost <= budget:
        return cuts
    else:
        return 0

