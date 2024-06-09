
def count_arrays(n, m):
    # Initialize a list to store the arrays
    arrays = []
    
    # Loop through all possible values of the first element
    for i in range(1, m + 1):
        # Add the first element to the array
        array = [i]
        
        # Loop through the remaining elements
        for j in range(1, n):
            # Add the next element to the array
            array.append(j)
            
            # Check if the array meets the conditions
            if is_valid_array(array, n, m):
                # Add the array to the list of valid arrays
                arrays.append(array)
        
    # Return the number of valid arrays
    return len(arrays)

def is_valid_array(array, n, m):
    # Check if the array has the correct length
    if len(array) != n:
        return False
    
    # Check if the array contains all integers from 1 to m
    for i in range(1, m + 1):
        if i not in array:
            return False
    
    # Check if the array has exactly one pair of equal elements
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] == array[j]:
                # Check if the array is strictly ascending before the i-th element and strictly descending after it
                if is_strictly_ascending_before_i_and_strictly_descending_after_i(array, i, n):
                    return True
    
    # If the array does not meet the conditions, return False
    return False

def is_strictly_ascending_before_i_and_strictly_descending_after_i(array, i, n):
    # Check if the array is strictly ascending before the i-th element
    for j in range(i):
        if array[j] >= array[j + 1]:
            return False
    
    # Check if the array is strictly descending after the i-th element
    for j in range(i + 1, n):
        if array[j] <= array[j - 1]:
            return False
    
    # If the array is strictly ascending before the i-th element and strictly descending after it, return True
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(count_arrays(n, m))

