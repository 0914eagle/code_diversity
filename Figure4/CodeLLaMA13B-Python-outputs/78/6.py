def hex_key(num):
    
    primes = [2, 3, 5, 7, 11, 13, 17]
    hex_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    hex_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    count = 0
    for i in num:
        if i.isdigit():
            if int(i) in primes:
                count += 1
        else:
            if hex_dict[i] in hex_primes:
                count += 1
    return count


print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))
