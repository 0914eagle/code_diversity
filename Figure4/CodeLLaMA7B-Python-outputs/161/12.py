def solve(s):
    
    # your code here
    return s.swapcase() if s.isalpha() else s[::-1]


if __name__ == '__main__':
    print("Example:")
    print(solve("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert solve("hello") == "olleh"
    assert solve("Ola") == "ola"
    assert solve("1234") == "4321"
    assert solve("hi!") == "hi!"
    assert solve("hi") == "hi"
    assert solve("") == ""
    assert solve("Ola-98") == "olA-98"
    assert solve("Ola-98!") == "olA-98!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
