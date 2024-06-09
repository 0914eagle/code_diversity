
def solve(arr):
    # Initialize variables to keep track of the sum and the minimum number of elements to insert
    sum_arr = 0
    min_elements = 0
    
    # Iterate through the array
    for i in range(len(arr)):
        # Add the current element to the sum
        sum_arr += arr[i]
        
        # If the sum is zero, we need to insert an element
        if sum_arr == 0:
            min_elements += 1
        
        # If the sum is negative, we need to insert elements to make the sum positive
        elif sum_arr < 0:
            min_elements += -sum_arr
        
    return min_elements

