
def get_max_cuts(sequence, budget):
    # Initialize variables
    n = len(sequence)
    odd_count = 0
    even_count = 0
    cuts = 0
    cost = 0

    # Iterate through the sequence
    for i in range(n):
        # Check if the current element is odd or even
        if sequence[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        # Check if the current element is the last element in the sequence
        if i == n - 1:
            # If the current element is odd, add it to the cost
            if sequence[i] % 2 == 1:
                cost += 1
            # Add the current element to the cuts
            cuts += 1

        # Check if the current element is not the last element in the sequence
        else:
            # If the current element is odd and the next element is even, add the cost of the cut
            if sequence[i] % 2 == 1 and sequence[i + 1] % 2 == 0:
                cost += 1
            # If the current element is even and the next element is odd, add the cost of the cut
            if sequence[i] % 2 == 0 and sequence[i + 1] % 2 == 1:
                cost += 1

            # Check if the cost is less than or equal to the budget
            if cost <= budget:
                # Add the current element to the cuts
                cuts += 1

    # Return the maximum number of cuts possible with the given budget
    return cuts

def main():
    # Read the input
    n, budget = map(int, input().split())
    sequence = list(map(int, input().split()))

    # Get the maximum number of cuts possible with the given budget
    max_cuts = get_max_cuts(sequence, budget)

    # Print the maximum number of cuts
    print(max_cuts)

if __name__ == '__main__':
    main()

