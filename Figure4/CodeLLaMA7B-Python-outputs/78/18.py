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
    hex_list = [hex_dict[x] for x in num]
    return sum(hex_list)


if __name__ == "__main__":
    print(hex_key("AB"))
    print(hex_key("1077E"))
    print(hex_key("AB