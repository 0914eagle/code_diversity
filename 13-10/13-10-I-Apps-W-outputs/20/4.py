
def get_subsequence_sum(sequence):
    # Initialize variables
    max_sum = -1
    current_sum = 0
    subsequence = []

    # Iterate through the sequence
    for i in range(len(sequence)):
        current_sum += sequence[i]
        subsequence.append(sequence[i])

        # If the current sum is odd and greater than the maximum sum, update the maximum sum and subsequence
        if current_sum % 2 == 1 and current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def main():
    # Read the input
    n = int(input())
    sequence = [int(x) for x in input().split()]

    # Find the subsequence with the maximum odd sum
    max_sum = get_subsequence_sum(sequence)

    # Print the result
    print(max_sum)

if __name__ == '__main__':
    main()

