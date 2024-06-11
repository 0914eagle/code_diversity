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
    if not lst:
        return 'Yes'
    if len(lst) == 1:
        return 'No'
    if len(lst) == 2:
        if lst[0] == ')' and lst[1] == '(':
            return 'Yes'
        else:
            return 'No'
    if len(lst) == 3:
        if lst[0] == ')' and lst[1] == '(' and lst[2] == ')':
            return 'Yes'
        else:
            return 'No'
    if len(lst) % 2 == 0:
        return 'No'
    if len(lst) % 2 != 0:
        return 'Yes'


if __name__ == '__main__':
    print(match_parens(['()(', ')']))
    print(match_parens([')', ')']))
    print(match_parens(['()', '()']))
    print(match_parens(['()', '(', ')']))
    print(match_parens(['(', ')', ')']))
    print(match_parens(['(', ')', '(', ')']))
    print(match_parens(['(', ')', '(', ')', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', '(', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', '(', ')', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', '(', ')', '(', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')']))
    print(match_parens(['(', ')', '(', ')', '(', ')', '(', ')', '(', ')', '(', ')', ')']))
    print(match_parens(['(', ')',