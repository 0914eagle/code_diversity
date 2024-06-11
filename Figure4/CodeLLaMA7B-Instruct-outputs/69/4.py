

def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Initialize the result and the frequency map
    result = -1
    freq_map = {}

    # Loop through the list and create a frequency map
    for num in lst:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

    # Find the greatest integer that meets the condition
    for num in freq_map:
        if freq_map[num] >= num and num > result:
            result = num

    return result


