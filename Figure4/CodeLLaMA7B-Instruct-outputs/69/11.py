

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
    # Initialize the result and the frequency of each integer
    result = -1
    freq = {}
    for i in lst:
        if i > 0:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    
    # Find the greatest integer that has a frequency greater than or equal to its value
    for i in freq:
        if freq[i] >= i and i > result:
            result = i
    
    # Return the result
    return result


