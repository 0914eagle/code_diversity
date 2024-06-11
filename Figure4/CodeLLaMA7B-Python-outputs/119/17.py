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
    # Opening parens
    open_parens = '('
    # Closing parens
    close_parens = ')'
    # Opening parens count
    open_parens_count = 0
    # Closing parens count
    close_parens_count = 0
    # Opening parens index
    open_parens_index = 0
    # Closing parens index
    close_parens_index = 0
    # Opening parens length
    open_parens_length = len(open_parens)
    # Closing parens length
    close_parens_length = len(close_parens)
    # Opening parens length
    lst_length = len(lst)
    # Opening parens index
    lst_index = 0
    # Opening parens index
    lst_index_1 = 1
    # Opening parens index
    lst_index_2 = 2
    # Opening parens index
    lst_index_3 = 3
    # Opening parens index
    lst_index_4 = 4
    # Opening parens index
    lst_index_5 = 5
    # Opening parens index
    lst_index_6 = 6
    # Opening parens index
    lst_index_7 = 7
    # Opening parens index
    lst_index_8 = 8
    # Opening parens index
    lst_index_9 = 9
    # Opening parens index
    lst_index_10 = 10
    # Opening parens index
    lst_index_11 = 11
    # Opening parens index
    lst_index_12 = 12
    # Opening parens index
    lst_index_13 = 13
    # Opening parens index
    lst_index_14 = 14
    # Opening parens index
    lst_index_15 = 15
    # Opening parens index
    lst_index_16 = 16
    # Opening parens index
    lst_index_17 = 17