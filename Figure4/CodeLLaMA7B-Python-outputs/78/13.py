def hex_key(num):
    
    hex_dict = {
        "0": 0,
        "1": 0,
        "2": 1,
        "3": 1,
        "4": 0,
        "5": 1,
        "6": 1,
        "7": 1,
        "8": 0,
        "9": 0,
        "A": 1,
        "B": 1,
        "C": 0,
        "D": 1,
        "E": 0,
        "F": 0,
    }
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_count = 0
    for i in num:
        prime_count += hex_dict[i]
    return prime_count


if