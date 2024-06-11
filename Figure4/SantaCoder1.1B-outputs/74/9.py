def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    if len(lst1) > len(lst2):
        return total_match(lst2, lst1)
    if len(lst1) < len(lst2):
        return total_match(lst1, lst2)
    if len(lst1) == len(lst2):
        if lst1[0] < lst2[0]:
            return lst1
        else:
            return lst2

print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))