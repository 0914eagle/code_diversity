def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if is_palindrome(q):
        return True
    if len(q) == 0:
        return False
    if len(q) == 1:
        return True
    if q[0] > w:
        return False
    if q[0] == w:
        return True
    if q[0] < w:
        return True
    return will_it_fly(q[1:], w)

print(will_it_fly([1, 2], 5))
print(will_it_fly([3, 2, 3], 1))
print(will_it_fly([3, 2, 3], 9))
print(will_it_fly([3], 5))
