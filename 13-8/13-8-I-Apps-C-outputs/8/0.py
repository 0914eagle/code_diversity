
def get_longest_exploration_sequence(arr, d, m):
    # Initialize the longest exploration sequence
    longest_seq = 0
    # Loop through each element in the array
    for i in range(len(arr)):
        # Get the length of the exploration sequence starting from the current element
        seq_length = get_exploration_sequence_length(arr, i, d, m)
        # If the length is greater than the current longest sequence, update the longest sequence
        if seq_length > longest_seq:
            longest_seq = seq_length
    # Return the longest exploration sequence
    return longest_seq

def get_exploration_sequence_length(arr, start, d, m):
    # Initialize the exploration sequence length
    seq_length = 1
    # Loop through each element in the array starting from the current element
    for i in range(start, len(arr)):
        # If the absolute difference between the current element and the previous element is greater than m, break the loop
        if abs(arr[i] - arr[i-1]) > m:
            break
        # If the distance between the current element and the previous element is greater than d, break the loop
        if i - start > d:
            break
        # Increment the exploration sequence length
        seq_length += 1
    # Return the exploration sequence length
    return seq_length

if __name__ == '__main__':
    n, d, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_longest_exploration_sequence(arr, d, m))

