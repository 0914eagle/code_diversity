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
    # your code here
    # 1. find the max value
    # 2. find the frequency of the max value
    # 3. compare the two
    # 4. return the max value if the frequency is greater than the value
    # 5. return -1 otherwise
    max_value = max(lst)
    max_value_freq = lst.count(max_value)
    if max_value_freq >= max_value:
        return max_value
    else:
        return -1


if