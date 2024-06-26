

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

    # Loop through the list and count the frequency of each integer
    for num in lst:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Find the greatest integer with frequency greater than or equal to its value
    for num, freq in freq_map.items():
        if freq >= num and num > result:
            result = num

    return result


