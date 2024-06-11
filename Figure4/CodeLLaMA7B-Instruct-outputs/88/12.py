

def sort_array(array):
    
    # Check if the array is empty
    if not array:
        return array

    # Calculate the sum of the first and last index values
    sum_first_last = array[0] + array[-1]

    # Sort the array in ascending order if the sum is odd, otherwise sort it in descending order
    if sum_first_last % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)


