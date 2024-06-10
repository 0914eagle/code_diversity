
def get_sorted_pairs(arr, x):
    # Initialize a set to store the sorted pairs
    sorted_pairs = set()
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Get the current element and its index
        curr_elem = arr[i]
        curr_index = i
        
        # Iterate over the remaining elements in the array
        for j in range(i+1, len(arr)):
            # Get the next element and its index
            next_elem = arr[j]
            next_index = j
            
            # Check if the current element is less than or equal to the next element
            if curr_elem <= next_elem:
                # Add the pair (curr_index, next_index) to the sorted pairs set
                sorted_pairs.add((curr_index, next_index))
    
    # Return the number of sorted pairs
    return len(sorted_pairs)

def main():
    # Read the input data
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Call the get_sorted_pairs function and print the result
    print(get_sorted_pairs(arr, x))

if __name__ == '__main__':
    main()

