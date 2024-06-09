
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def find_min_diff(A, K, Q):
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Loop through all possible starting indices
    for i in range(N - K + 1):
        # Find the minimum element in the subsequence
        min_elem = min(A[i:i+K])
        # Find the index of the minimum element in the subsequence
        min_index = A[i:i+K].index(min_elem)
        # Remove the minimum element from the subsequence
        A[i+min_index] = float('inf')
        # Find the new minimum and maximum elements in the subsequence
        new_min = min(A[i:i+K])
        new_max = max(A[i:i+K])
        # Calculate the difference between the new minimum and maximum elements
        diff = new_max - new_min
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    return min_diff

def main():
    N, K, Q, A = read_input()
    print(find_min_diff(A, K, Q))

if __name__ == '__main__':
    main()

