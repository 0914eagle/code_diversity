
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def optimize_sequence(A, K, Q):
    # Initialize the smallest and largest values removed as infinity and -infinity, respectively
    smallest, largest = float('inf'), -float('inf')
    
    # Loop through each contiguous subsequence of length K
    for i in range(N-K+1):
        # Find the minimum element in the subsequence
        min_elem = min(A[i:i+K])
        # Update the smallest and largest values removed
        smallest = min(smallest, min_elem)
        largest = max(largest, min_elem)
    
    # Return the difference between the smallest and largest values removed
    return largest - smallest

def main():
    N, K, Q, A = read_input()
    print(optimize_sequence(A, K, Q))

if __name__ == '__main__':
    main()

