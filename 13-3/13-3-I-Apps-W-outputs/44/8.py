
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
            # Check if the number of odd and even elements is equal
            if odd_count == even_count:
                # Increment the number of cuts
                cuts += 1
            else:
                # Calculate the cost of the current cut
                cost += abs(odd_count - even_count)

                # Check if the cost is less than or equal to the budget
                if cost <= budget:
                    # Increment the number of cuts
                    cuts += 1
                else:
                    # Break the loop
                    break
        else:
            # Check if the number of odd and even elements is equal
            if odd_count == even_count:
                # Increment the number of cuts
                cuts += 1
            else:
                # Calculate the cost of the current cut
                cost += abs(odd_count - even_count)

                # Check if the cost is less than or equal to the budget
                if cost <= budget:
                    # Increment the number of cuts
                    cuts += 1
                else:
                    # Break the loop
                    break

    # Return the maximum number of cuts
    return cuts

def main():
    # Read the input
    n, budget = map(int, input().split())
    sequence = list(map(int, input().split()))

    # Get the maximum number of cuts
    max_cuts = get_max_cuts(sequence, budget)

    # Print the result
    print(max_cuts)

if __name__ == '__main__':
    main()

