
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def solve(N, K, Q, A):
    # Initialize the minimum and maximum values
    min_val, max_val = float('inf'), -float('inf')
    
    # Perform the Q operations
    for i in range(Q):
        # Find the smallest element in the current subsequence
        smallest = min(A[i:i+K])
        # Update the minimum and maximum values
        min_val = min(min_val, smallest)
        max_val = max(max_val, smallest)
        # Remove the smallest element from the subsequence
        A = A[:i] + A[i+1:i+K] + A[i+K:]
    
    # Return the difference between the minimum and maximum values
    return max_val - min_val

def main():
    N, K, Q, A = read_input()
    print(solve(N, K, Q, A))

if __name__ == '__main__':
    main()

