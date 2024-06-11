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
    # Your code here
    # 1. find the max value in the list
    # 2. check if the max value is greater than 0
    # 3. check if the frequency of the max value is greater than or equal to the value of the integer itself
    # 4. if all the above conditions are true, return the max value
    # 5. if any of the above conditions are false, return -1
    # 6. if the list is empty, return -1
    
    if lst == []:
        return -1
    else:
        max_value = max(lst)
        if max_value > 0 and lst.count(max_value) >= max_value:
            return max_value
        else:
            return -1

print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
print(search([]))
