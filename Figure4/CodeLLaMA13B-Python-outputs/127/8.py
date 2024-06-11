def intersection(interval1, interval2):
    

    # your code here
    # return "YES" if the intersection is a prime number, otherwise return "NO"
    # if the two intervals don't intersect, return "NO"
    pass


if __name__ == '__main__':
    print("Example:")
    print(intersection((1, 2), (2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    print("Coding complete? Click 'Check' to earn cool rewards!")
