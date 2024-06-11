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
    # Write your code here
    if len(lst) == 0:
        return -1
    else:
        max_val = lst[0]
        max_freq = 1
        for i in range(1, len(lst)):
            if lst[i] > max_val:
                max_val = lst[i]
                max_freq = 1
            elif lst[i] == max_val:
                max_freq += 1
        if max_freq >= len(lst):
            return max_val
        else:
            return -1

if __name__ == '__main__':
    lst = [4, 1, 2, 2, 3, 1]
    print(search(lst))