def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for i in num:
        if i in "0123456789":
            if int(i) in primes:
                count += 1
        elif i in "ABCDEF":
            if int(i, 16) in primes:
                count += 1
    return count


if __name__ == "__main__":
    print(hex_key("AB"))
    print(hex_key("1077E"))
    print(hex_key("ABED1A33"))
    print(hex_key("123456789ABCDEF0"))
    print(hex_key("2020"))
