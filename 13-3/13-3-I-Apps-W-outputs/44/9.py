
def get_max_cuts(sequence, budget):
    # Initialize variables
    max_cuts = 0
    current_budget = 0
    cuts = []

    # Iterate through the sequence
    for i in range(len(sequence)):
        # Check if the current element is even or odd
        if sequence[i] % 2 == 0:
            # If the current element is even, check if the previous element is odd
            if i > 0 and sequence[i-1] % 2 == 1:
                # If the previous element is odd, calculate the cost of the cut
                cost = abs(sequence[i-1] - sequence[i])
                # Check if the cost is within budget
                if current_budget + cost <= budget:
                    # If the cost is within budget, add the cut to the list of cuts
                    cuts.append(i)
                    current_budget += cost
                    max_cuts += 1
        else:
            # If the current element is odd, check if the next element is even
            if i < len(sequence)-1 and sequence[i+1] % 2 == 0:
                # If the next element is even, calculate the cost of the cut
                cost = abs(sequence[i] - sequence[i+1])
                # Check if the cost is within budget
                if current_budget + cost <= budget:
                    # If the cost is within budget, add the cut to the list of cuts
                    cuts.append(i+1)
                    current_budget += cost
                    max_cuts += 1

    # Return the maximum number of cuts that can be made within the budget
    return max_cuts

def main():
    # Read the input
    n, budget = map(int, input().split())
    sequence = list(map(int, input().split()))

    # Call the function to get the maximum number of cuts
    max_cuts = get_max_cuts(sequence, budget)

    # Print the result
    print(max_cuts)

if __name__ == '__main__':
    main()

