
def get_optimal_subsequence(sequence, k, q):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    # Initialize the optimal subsequence as the first k elements
    optimal_subsequence = sequence[:k]
    # Initialize the largest and smallest elements removed as the first element of the subsequence
    largest_removed, smallest_removed = optimal_subsequence[0], optimal_subsequence[0]
    # Loop through the remaining elements
    for i in range(k, len(sequence)):
        # Add the current element to the subsequence
        optimal_subsequence.append(sequence[i])
        # Remove the smallest element from the subsequence
        optimal_subsequence.remove(min(optimal_subsequence))
        # Update the largest and smallest elements removed
        largest_removed = max(largest_removed, sequence[i])
        smallest_removed = min(smallest_removed, sequence[i])
    # Return the difference between the largest and smallest elements removed
    return largest_removed - smallest_removed

def solve(sequence, k, q):
    # Initialize the optimal subsequence as the first k elements
    optimal_subsequence = sequence[:k]
    # Loop through the remaining elements
    for i in range(k, len(sequence)):
        # Add the current element to the subsequence
        optimal_subsequence.append(sequence[i])
        # Remove the smallest element from the subsequence
        optimal_subsequence.remove(min(optimal_subsequence))
        # Update the optimal subsequence if the current subsequence is better
        if get_optimal_subsequence(optimal_subsequence, k, q) < get_optimal_subsequence(sequence[i+1:], k, q-1):
            sequence = sequence[:i+1] + sequence[i+2:]
    # Return the optimal subsequence
    return optimal_subsequence

if __name__ == '__main__':
    n, k, q = map(int, input().split())
    sequence = list(map(int, input().split()))
    print(solve(sequence, k, q))

