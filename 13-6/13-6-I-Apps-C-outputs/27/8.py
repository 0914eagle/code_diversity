
def get_permutation(n, m, k, a):
    # Initialize the permutation with the first critic
    permutation = [1]
    # Initialize the average score with the first critic's score
    average_score = a[0]
    # Iterate over the remaining critics
    for i in range(1, n):
        # Calculate the average score of the previous critics
        previous_average_score = average_score / i
        # If the current critic's score is higher than the average score, give them a score of 0
        if a[i] > previous_average_score:
            permutation.append(0)
        # Otherwise, give them a score of m
        else:
            permutation.append(m)
        # Update the average score with the current critic's score
        average_score += a[i]
    # Return the permutation
    return permutation

def main():
    # Read the input
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    # Get the permutation
    permutation = get_permutation(n, m, k, a)
    # Print the permutation
    print(*permutation)

if __name__ == '__main__':
    main()

