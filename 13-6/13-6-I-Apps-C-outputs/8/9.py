
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def solve(N, K, Q, A):
    # Initialize the smallest and largest values
    smallest, largest = float('inf'), -float('inf')
    
    # Perform the Q operations
    for i in range(Q):
        # Find the smallest element in the contiguous subsequence of length K
        smallest_element = min(A[i:i+K])
        
        # Remove the smallest element from the sequence
        A.remove(smallest_element)
        
        # Update the smallest and largest values
        smallest = min(smallest, smallest_element)
        largest = max(largest, smallest_element)
    
    # Return the difference between the smallest and largest values
    return largest - smallest

if __name__ == '__main__':
    N, K, Q, A = read_input()
    print(solve(N, K, Q, A))

