
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def optimize_sequence(A, K):
    # Initialize the smallest and largest elements removed
    smallest, largest = float('inf'), -float('inf')
    
    # Loop through each possible contiguous subsequence of length K
    for i in range(len(A) - K + 1):
        # Find the smallest and largest elements in the subsequence
        subsequence_smallest, subsequence_largest = float('inf'), -float('inf')
        for j in range(i, i + K):
            if A[j] < subsequence_smallest:
                subsequence_smallest = A[j]
            if A[j] > subsequence_largest:
                subsequence_largest = A[j]
        
        # Update the smallest and largest elements removed
        if subsequence_smallest < smallest:
            smallest = subsequence_smallest
        if subsequence_largest > largest:
            largest = subsequence_largest
    
    return largest - smallest

def main():
    N, K, Q, A = read_input()
    print(optimize_sequence(A, K))

if __name__ == '__main__':
    main()

