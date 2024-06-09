
def get_min_sum(arr):
    # Initialize variables
    n = len(arr)
    sum_of_non_deleted_elements = 0
    parity = 0
    deleted_elements = set()
    
    # Iterate through the array
    for i in range(n):
        # If the current element is not deleted, add its value to the sum
        if i not in deleted_elements:
            sum_of_non_deleted_elements += arr[i]
        
        # If it is the first move, choose any element and delete it
        if len(deleted_elements) == 0:
            deleted_elements.add(i)
        
        # If it is the second or any next move:
        # If the last deleted element was odd, choose any even element and delete it
        # If the last deleted element was even, choose any odd element and delete it
        else:
            # Get the last deleted element
            last_deleted_element = deleted_elements.pop()
            
            # If the last deleted element was odd, choose any even element and delete it
            if last_deleted_element % 2 == 1:
                for j in range(i, n):
                    if arr[j] % 2 == 0 and j not in deleted_elements:
                        deleted_elements.add(j)
                        break
            
            # If the last deleted element was even, choose any odd element and delete it
            else:
                for j in range(i, n):
                    if arr[j] % 2 == 1 and j not in deleted_elements:
                        deleted_elements.add(j)
                        break
    
    # Return the minimum possible sum of non-deleted elements
    return sum_of_non_deleted_elements

