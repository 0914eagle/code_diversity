def select_words(s, n):
    
    # your code here
    pass


if __name__ == '__main__':
    print("Example:")
    print(list(select_words('Mary had a little lamb', 4)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(select_words('Mary had a little lamb', 4)) == ['little']
    assert list(select_words('Mary had a little lamb', 3)) == ['Mary', 'lamb']
    assert list(select_words('simple white space', 2)) == []
    assert list(select_words('Hello world', 4)) == ['world']
    assert list(select_words('Uncle sam', 3)) == ['Uncle']
    print("Coding complete? Click 'Check' to earn cool rewards!")
