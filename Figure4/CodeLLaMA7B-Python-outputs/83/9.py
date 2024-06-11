def starts_one_ends(n):
    
    count = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            count += 1
    return count


if __name__ == "__main__":
    print(starts_one_ends(1))
    print(starts_one_ends(2))
    print(starts_one_ends(3))
    print(starts_one_ends(4))
