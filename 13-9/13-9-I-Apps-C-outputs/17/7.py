
def solve(A, K, Q):
    # Step 1: Sort the array A
    A.sort()
    
    # Step 2: Initialize the smallest and largest values
    smallest, largest = A[0], A[0]
    
    # Step 3: Loop through the Q operations
    for i in range(Q):
        # Step 3.1: Find the contiguous subsequence of length K
        subsequence = A[i:i+K]
        
        # Step 3.2: Remove the smallest element from the subsequence
        smallest = min(subsequence)
        subsequence.remove(smallest)
        
        # Step 3.3: Update the largest value
        largest = max(subsequence)
    
    # Step 4: Return the difference between the smallest and largest values
    return largest - smallest

def main():
    # Read the input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Solve the problem
    result = solve(A, K, Q)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

