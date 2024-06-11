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
    stack = []
    for s in lst:
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return 'No'
                stack.pop()
    return 'Yes' if not stack else 'No'
/tests/test_arrays.py
from nose.tools import assert_equal
from nose.tools import assert_raises
from nose.tools import raises

from arrays import (
    find_missing_number,
    find_missing_number_2,
    find_missing_number_3,
    find_missing_number_4,
    find_missing_number_5,
    find_missing_number_6,
    find_missing_number_7,
    find_missing_number_8,
    find_missing_number_9,
    find_missing_number_10,
    find_missing_number_11,
    find_missing_number_12,
    find_missing_number_13,
    find_missing_number_14,
    find_missing_number_15,
    find_missing_number_16,
    find_missing_number_17,
    find_missing_number_18,
    find_missing_number_19,
    find_missing_number_20,
    find_missing_number_21,
    find_missing_number_22,
    find_missing_number_23,
    find_missing_number_24,
    find_missing_number_25,
    find_missing_number_26,
    find_missing_number_27,
    find_missing_number_28,
    find_missing_number_29,
    find_missing_number_30,
    find_missing_number_31,
    find_missing_number_32,
    find_missing_number_33,
    find_missing_number_34,
    find_missing_number_35,
    find_missing_number_36,
    find_missing_number_37,
    find_missing_number_38,
    find_missing_number_39,
    find_missing_number_40,
    find_missing_number_41,
    find_missing_number_42,