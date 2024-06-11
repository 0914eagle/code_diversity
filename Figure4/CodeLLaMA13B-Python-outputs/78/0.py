def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for i in num:
        if i in "2357BD":
            count += 1
        elif i == "A":
            count += 1
        elif i == "E":
            count += 1
        elif i == "1":
            count += 1
    return count


print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))
