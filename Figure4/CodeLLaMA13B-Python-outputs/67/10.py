def fruit_distribution(s,n):
    
    # your code here
    return n - int(s.split()[0]) - int(s.split()[2])


if __name__ == '__main__':
    print("Example:")
    print(fruit_distribution("5 apples and 6 oranges", 19))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
    print("Coding complete? Click 'Check' to earn cool rewards!")
