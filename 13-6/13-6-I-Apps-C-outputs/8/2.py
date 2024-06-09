
def get_smallest_difference(sequence, k, q):
    
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the smallest and largest elements removed
    smallest, largest = None, None
    
    # Loop through each operation
    for i in range(q):
        # Get the subsequence of length k starting from the current index
        subsequence = sequence[i:i+k]
        
        # Remove the smallest element from the subsequence
        smallest_element = min(subsequence)
        subsequence.remove(smallest_element)
        
        # Update the smallest and largest elements removed
        if smallest is None or smallest_element < smallest:
            smallest = smallest_element
        if largest is None or largest < smallest_element:
            largest = smallest_element
    
    # Return the smallest possible value of the difference between the largest and smallest elements removed
    return largest - smallest

def main():
    # Read the input sequence, k, and q from stdin
    n, k, q = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # Call the get_smallest_difference function and print the result
    print(get_smallest_difference(sequence, k, q))

if __name__ == '__main__':
    main()

