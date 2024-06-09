
def count_arrays(n, m):
    # Initialize a list to store the arrays
    arrays = []
    
    # Iterate over all possible values of the first element
    for i in range(1, m + 1):
        # Add the first element to the array
        array = [i]
        
        # Iterate over the remaining elements
        for j in range(1, n):
            # Add a new element to the array
            array.append(j)
            
            # Check if the array meets the conditions
            if is_valid_array(array, n, m):
                # Add the array to the list of arrays
                arrays.append(array)
        
    # Return the number of arrays
    return len(arrays)

def is_valid_array(array, n, m):
    # Check if the array has the correct length
    if len(array) != n:
        return False
    
    # Check if the array has exactly one pair of equal elements
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] == array[j]:
                count += 1
                break
        if count > 1:
            return False
    
    # Check if the array is strictly ascending or descending
    is_ascending = True
    is_descending = True
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            is_ascending = False
        if array[i] < array[i + 1]:
            is_descending = False
    if not (is_ascending or is_descending):
        return False
    
    # Return True if the array meets all conditions
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(count_arrays(n, m))

