
def max_sum_after_modifying_array(arr, k):
    # Step 1: Sort the array in descending order
    arr.sort(reverse=True)
    
    # Step 2: Initialize a variable to keep track of the number of positive elements
    num_positive = 0
    
    # Step 3: Iterate through the array and count the number of positive elements
    for i in range(len(arr)):
        if arr[i] > 0:
            num_positive += 1
    
    # Step 4: If the number of positive elements is greater than the number of negative elements, return the sum of the array
    if num_positive > len(arr) - num_positive:
        return sum(arr)
    
    # Step 5: Otherwise, iterate through the array and find the first negative element
    for i in range(len(arr)):
        if arr[i] < 0:
            break
    
    # Step 6: Flip the sign of the first negative element and return the sum of the array
    arr[i] = -arr[i]
    return sum(arr)

