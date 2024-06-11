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
    if string[0] == ']' or string[-1] == '[':
        return False

    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if stack:
                stack.pop()
            else:
                return False
    return True if stack else False


if __name__ == '__main__':
    print(is_nested('[[]]'))
    print(is_nested('[]]]]]]][[[[[]'))
    print(is_nested('[][]'))
    print(is_nested('[]'))
    print(is_nested('[[][]]'))
    print(is_nested('[[]][['))
