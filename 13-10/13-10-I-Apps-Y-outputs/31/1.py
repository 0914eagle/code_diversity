
def get_next_string(s):
    next_s = ""
    for c in s:
        if c == "1":
            next_s += "1"
        elif c == "2":
            next_s += "22"
        elif c == "3":
            next_s += "333"
        elif c == "4":
            next_s += "4444"
        elif c == "5":
            next_s += "55555"
        elif c == "6":
            next_s += "666666"
        elif c == "7":
            next_s += "7777777"
        elif c == "8":
            next_s += "88888888"
        elif c == "9":
            next_s += "999999999"
    return next_s

def get_kth_char(s, k):
    curr_len = len(s)
    if k <= curr_len:
        return s[k-1]
    else:
        return get_kth_char(get_next_string(s), k-curr_len)

if __name__ == '__main__':
    s = input()
    k = int(input())
    print(get_kth_char(s, k))

