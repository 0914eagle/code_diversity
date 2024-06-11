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
    if len(string) == 0:
        return False
    if string[0] == '[' and string[-1] == ']':
        return True
    else:
        return False

# print(is_nested('[]'))
# print(is_nested('[][]'))
# print(is_nested('[[]]'))
# print(is_nested('[[]][['))
# print(is_nested('[]]]]]]][[[[[]'))

