def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # your code here
    return a == int(round(a ** (1/3))) ** 3


if __name__ == '__main__':
    print("Example:")
    print(iscube(125))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert iscube(125) == True
    assert iscube(64) == True
    assert iscube(8) == False
    assert iscube(1) == True
    assert iscube(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
