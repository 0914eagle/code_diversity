
def get_optimal_subsequence(sequence, k, q):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the smallest and largest elements removed
    smallest, largest = 0, 0
    
    # Loop through each contiguous subsequence of length k
    for i in range(len(sequence) - k + 1):
        # Get the subsequence
        subsequence = sequence[i:i+k]
        
        # Remove the smallest element from the subsequence
        smallest_element = subsequence.pop(subsequence.index(min(subsequence)))
        
        # Update the smallest and largest elements removed
        smallest = min(smallest, smallest_element)
        largest = max(largest, smallest_element)
        
    # Return the difference between the largest and smallest elements removed
    return largest - smallest

def main():
    # Read the input
    n, k, q = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # Call the function to get the optimal subsequence
    optimal_subsequence = get_optimal_subsequence(sequence, k, q)
    
    # Print the smallest possible value of X-Y
    print(optimal_subsequence)

if __name__ == '__main__':
    main()

