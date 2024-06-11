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
        "C": 1,
        "D": 1,
        "E": 1,
        "F": 1,
    }
    hex_list = list(num)
    hex_count = 0
    for i in hex_list:
        if hex_dict[i] == 1:
            hex_count += 1
    return hex_count


if