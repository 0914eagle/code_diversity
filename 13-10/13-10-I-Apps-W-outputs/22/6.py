
def get_sorted_pairs(arr, x):
    # Initialize a set to store the sorted pairs
    sorted_pairs = set()
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Get the current element and its index
        curr_element = arr[i]
        curr_index = i + 1
        
        # Iterate over the remaining elements in the array
        for j in range(curr_index, len(arr)):
            # Get the next element and its index
            next_element = arr[j]
            next_index = j + 1
            
            # Check if the current element is less than or equal to the next element
            if curr_element <= next_element:
                # Add the current element to the set of sorted pairs
                sorted_pairs.add((curr_element, next_element))
                
                # Check if the current element is equal to the next element
                if curr_element == next_element:
                    # Add the next element to the set of sorted pairs
                    sorted_pairs.add((next_element, next_element))
    
    # Return the number of sorted pairs
    return len(sorted_pairs)

def main():
    # Read the input data
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Print the number of sorted pairs
    print(get_sorted_pairs(arr, x))

if __name__ == '__main__':
    main()

