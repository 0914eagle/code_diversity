def starts_one_ends(n):
    
    # 10**(n-1) is the largest n-digit number
    # 10**(n-1) + 1 is the smallest n+1-digit number
    return (10**(n-1) + 1 - 10**(n-1)) * 2


if __name__ == '__main__':
    print(starts_one_ends(1))
    print(starts_one_ends(2))
    print(starts_one_ends(3))
    print(starts_one_ends(4))
    print(starts_one_ends(5))
    print(starts_one_ends(6))
    print(starts_one_ends(7))
    print(starts_one_ends(8))
    print(starts_one_ends(9))
    print(starts_one_ends(10))
