
def get_new_string(s, day):
    new_s = ""
    for char in s:
        if char == "2":
            new_s += "22"
        elif char == "3":
            new_s += "333"
        elif char == "4":
            new_s += "4444"
        elif char == "5":
            new_s += "55555"
        elif char == "6":
            new_s += "666666"
        elif char == "7":
            new_s += "7777777"
        elif char == "8":
            new_s += "88888888"
        elif char == "9":
            new_s += "999999999"
        else:
            new_s += char
    return new_s

def get_string_after_days(s, days):
    current_s = s
    for i in range(days):
        current_s = get_new_string(current_s, i)
    return current_s

def get_kth_char(s, k):
    return s[k-1]

if __name__ == '__main__':
    s = input()
    k = int(input())
    days = 5 * (10**15)
    current_s = get_string_after_days(s, days)
    print(get_kth_char(current_s, k))

