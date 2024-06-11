def sorted_list_sum(lst):
    
    # your code here
    # lst = [x for x in lst if len(x) % 2 == 0]
    # lst.sort(key=len)
    # return lst
    return sorted([x for x in lst if len(x) % 2 == 0], key=len)


if __name__ == '__main__':
    print("Example:")
    print(sorted_list_sum(['a', 'aa', 'aaa', 'b']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sorted_list_sum(['a', 'aa', 'aaa', 'b']) == ['aa', 'aaa']
    assert sorted_list_sum(['a', 'b', 'c']) == []
    assert sorted_list_sum(['a']) == ['a']
    assert sorted_list_sum(['']) == []
    assert sorted_list_sum(['a', 'a']) == ['a', 'a']
    print("Coding complete? Click 'Check' to earn cool rewards!")
