
def get_next_day_string(current_string):
    next_string = ""
    for char in current_string:
        if char == "2":
            next_string += "22"
        elif char == "3":
            next_string += "333"
        elif char == "4":
            next_string += "4444"
        elif char == "5":
            next_string += "55555"
        elif char == "6":
            next_string += "666666"
        elif char == "7":
            next_string += "7777777"
        elif char == "8":
            next_string += "88888888"
        elif char == "9":
            next_string += "999999999"
        else:
            next_string += char
    return next_string

def get_kth_char_after_n_days(n, k):
    current_string = input()
    for i in range(n):
        current_string = get_next_day_string(current_string)
    return current_string[k-1]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(get_kth_char_after_n_days(n, k))

