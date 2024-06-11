def sorted_list_sum(lst):
    
    return sorted(list(filter(lambda x: len(x) % 2 == 0, lst)), key=len)


if __name__ == '__main__':
    print("Example:")
    print(sorted_list_sum(['aa', 'a', 'aaa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sorted_list_sum(['aa', 'a', 'aaa']) == ['aa']
    assert sorted_list_sum(['et', 'ec', 'erk', 'et', 'ec', 'et']) == ['et', 'et', 'et']
    assert sorted_list_sum(['et', 'ec', 'erk', 'et', 'ec', 'et', 'aa']) == ['et', 'et', 'et', 'aa']
    print("Coding complete? Click 'Check' to earn cool rewards!")
