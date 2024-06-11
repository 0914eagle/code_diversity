def solve(N):
    
    # your code here
    return bin(N)[2:].replace("0", "1").replace("1", "0")


if __name__ == '__main__':
    print("Example:")
    print(solve(1000))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert solve(1000) == "1"
    assert solve(150