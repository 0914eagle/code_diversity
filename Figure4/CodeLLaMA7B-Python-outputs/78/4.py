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
        "B": 3,
        "C": 1,
        "D": 3,
        "E": 1,
        "F": 3,
    }
    hex_list = [hex_dict[i] for i in num]
    return sum(hex_list)


if __name__ == "__main__":
    print(