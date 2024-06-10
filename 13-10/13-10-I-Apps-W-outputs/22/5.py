
def get_sorted_pairs(arr, x):
    # Initialize a set to store the pairs
    pairs = set()
    
    # Loop through each element in the array
    for i in range(len(arr)):
        # Get the current element
        current = arr[i]
        
        # Loop through each element after the current element
        for j in range(i+1, len(arr)):
            # Get the next element
            next = arr[j]
            
            # If the next element is greater than the current element, add the pair to the set
            if next > current:
                pairs.add((current, next))
    
    # Return the number of pairs
    return len(pairs)

def main():
    # Read the input
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Call the get_sorted_pairs function
    result = get_sorted_pairs(arr, x)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

