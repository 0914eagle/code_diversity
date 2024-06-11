def sorted_list_sum(lst):
    
    # your code here
    # lst = [x for x in lst if len(x) % 2 == 0]
    # lst.sort(key=len)
    # return lst
    return sorted(filter(lambda x: len(x) % 2 == 0, lst), key=len)


if __name__ == '__main__':
    print("Example:")
    print(list(sorted_list_sum(["aa", "a", "aaa"])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(sorted_list_sum(["aa", "a", "aaa"])) == ["aa"]
    assert list(sorted_list_sum(["ab", "a", "aaa", "cd"])) == ["ab", "cd"]
    assert list(sorted_list_sum(["abc", "a", "b"])) == []
    assert list(sorted_list_sum(["a", "a", "a", "a", "b", "b", "c"])) == ["a", "a", "b", "b", "c"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
