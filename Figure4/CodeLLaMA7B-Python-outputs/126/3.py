def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # Base case
    if len(lst) <= 1:
        return True
    # Recursive case
    else:
        # Check if first and last elements are equal
        if lst[0] == lst[-1]:
            # Check if middle element is equal to first or last
            if lst[len(lst)//2] == lst[0] or lst[len(lst)//2] == lst[-1]:
                return is_sorted(lst[:len(lst)//2])
            else:
                return False
        # Check if first and last elements are not equal
        elif lst[0] != lst[-1]:
            # Check if middle element is equal to first or last
            if lst[len(lst)//2] == lst[0] or lst[len(lst)//2] == lst[-1]:
                return False
            # Check if middle element is greater than first and less than last
            elif lst[len(lst)//2] > lst[0] and lst[len(lst)//2] < lst[-1]:
                return is_sorted(lst[:len(lst)//2]) and is_sorted(lst[len(lst)//2:])
            # Check if middle element is less than first and greater than last
            elif lst[len(lst)//2] < lst[0] and lst[len(lst)//2] > lst[-1]:
                return is_sorted(lst[:len(lst)//2]) and is_sorted(lst[len(lst)//2:])
            # If middle element is neither greater nor less than first and last
            else:
                return False


print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([1, 2, 3, 4, 5, 6]))
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))
print(is_sorted([1, 2, 2, 