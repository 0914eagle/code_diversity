
def get_optimal_value(A, K, Q):
    # Sort the array in ascending order
    A.sort()
    # Initialize the optimal value to zero
    optimal_value = 0
    # Loop through each contiguous subsequence of length K
    for i in range(len(A) - K + 1):
        # Get the smallest element in the subsequence
        smallest_element = A[i]
        # Get the largest element in the subsequence
        largest_element = A[i + K - 1]
        # Update the optimal value
        optimal_value = max(optimal_value, largest_element - smallest_element)
    # Return the optimal value
    return optimal_value

def main():
    # Read the input from stdin
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    # Call the get_optimal_value function and print the result
    print(get_optimal_value(A, K, Q))

if __name__ == '__main__':
    main()

