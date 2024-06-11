def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    # Your code here
    stack = []
    for i in lst:
        for j in i:
            if j == '(':
                stack.append(j)
            elif j == ')':
                if len(stack) == 0:
                    return 'No'
                else:
                    stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    print("Example:")
    print(match_parens(['()(', ')']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens([')', ')']) == 'No'
    assert match_parens([(')', '(', ')', '(', ')', '(', ')', ')', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')',
                         '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')',