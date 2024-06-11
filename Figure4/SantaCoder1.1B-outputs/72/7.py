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
    # Your code here
    if len(q) == 1:
        return True
    if len(q) == 2:
        return q[0] == q[1]
    if len(q) == 3:
        return q[0] == q[1] and q[1] == q[2]
    if len(q) == 4:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3]
    if len(q) == 5:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[3] == q[4]
    if len(q) == 6:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[3] == q[4] and q[4] == q[5]
    if len(q) == 7:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[3] == q[4] and q[4] == q[5] and q[5] == q[6]
    if len(q) == 8:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[3] == q[4] and q[4] == q[5] and q[5] == q[6] and q[6] == q[7]
    if len(q) == 9:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[3] == q[4] and q[4] == q[5] and q[5] == q[6] and q[6] == q[7] and q[7] == q[8]
    if len(q) == 10:
        return q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[3