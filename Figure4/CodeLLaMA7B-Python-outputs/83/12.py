def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that has n-1 digits
    return (10**(n-1) - 10**(n-2)) * 2


if __name__ == "__main__":
    print(starts_one_ends(1))
    print(starts_one_ends(2))
    print(starts_one_ends(3))
    print(starts_one_ends(4))
    print(starts_one_ends(5))
