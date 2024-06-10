
def get_longest_exploration_sequence(arr, d, m):
    # Initialize variables
    n = len(arr)
    longest_sequence = 0
    visited = [False] * n
    # Loop through each element in the array
    for i in range(n):
        # If the element has not been visited before
        if not visited[i]:
            # Mark the element as visited and calculate the length of the sequence
            visited[i] = True
            sequence_length = 1
            # Loop through the neighbors of the current element
            for j in range(i+1, min(n, i+d+1)):
                # If the neighbor has not been visited before and the difference between the current element and the neighbor is at most m
                if not visited[j] and abs(arr[i] - arr[j]) <= m:
                    # Mark the neighbor as visited and increment the sequence length
                    visited[j] = True
                    sequence_length += 1
            # If the sequence length is greater than the longest sequence length seen so far
            if sequence_length > longest_sequence:
                # Update the longest sequence length
                longest_sequence = sequence_length
    return longest_sequence

def main():
    n, d, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_longest_exploration_sequence(arr, d, m))

if __name__ == '__main__':
    main()

