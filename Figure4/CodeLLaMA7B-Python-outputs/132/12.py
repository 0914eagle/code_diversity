def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # My solution
    # return string.count('[]') > 0

    # Given solution
    if string.count('[]') == 0:
        return False

    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) == 0:
                return True
            stack.pop()
    return False


