
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def find_smallest_difference(A, K):
    # Find the smallest element in the subsequence
    smallest = min(A[:K])
    # Find the index of the smallest element in the subsequence
    smallest_index = A.index(smallest)
    # Remove the smallest element from the subsequence
    A.pop(smallest_index)
    # Return the smallest element and the subsequence without it
    return smallest, A

def solve(N, K, Q, A):
    # Initialize the smallest difference
    smallest_difference = float('inf')
    # Loop through each operation
    for i in range(Q):
        # Find the smallest element in the subsequence and the subsequence without it
        smallest, subsequence = find_smallest_difference(A, K)
        # Update the smallest difference
        smallest_difference = min(smallest_difference, smallest)
        # Update the subsequence
        A = subsequence
    # Return the smallest difference
    return smallest_difference

if __name__ == '__main__':
    N, K, Q, A = read_input()
    print(solve(N, K, Q, A))

