
def get_next_string(s):
    next_string = ""
    for char in s:
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

def get_kth_char(s, k):
    day = 0
    while len(s) < k:
        s = get_next_string(s)
        day += 1
    return s[k-1]

def main():
    s = input()
    k = int(input())
    print(get_kth_char(s, k))

if __name__ == '__main__':
    main()

