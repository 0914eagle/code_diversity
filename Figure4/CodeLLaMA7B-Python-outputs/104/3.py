def unique_digits(x):
    
    # Your code here
    return sorted(list(set([x for x in x if not any(i in str(x) for i in '2468')])))


if __name__ == '__main__':
    print("Example:")
    print(unique_digits([15, 33, 1422, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([123, 1235, 500, 5]) == []
    assert unique_digits([555, 333, 1, 2, 22]) == [1, 2]
    print("Coding complete? Click 'Check' to earn cool rewards!")
