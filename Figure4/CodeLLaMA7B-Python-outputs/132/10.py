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
    # return True if string.count('[]') % 2 == 1 else False

    # Given solution
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
        elif char == ']' and not stack:
            return True
    return False


# print(is_nested('[[]]'))
# print(is_nested('[]]]]]]][[[[[]'))
# print(is_nested('[][]'))
# print(is_nested('[]'))
# print(is_nested('[[][]]'))
# print(is_nested('[[]][['))
