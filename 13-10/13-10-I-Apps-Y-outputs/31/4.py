
def get_next_day(s):
    result = ""
    for c in s:
        if c == "1":
            result += "1"
        elif c == "2":
            result += "22"
        elif c == "3":
            result += "333"
        elif c == "4":
            result += "4444"
        elif c == "5":
            result += "55555"
        elif c == "6":
            result += "666666"
        elif c == "7":
            result += "7777777"
        elif c == "8":
            result += "88888888"
        elif c == "9":
            result += "999999999"
    return result

def get_kth_char(s, k):
    count = 1
    for c in s:
        if count == k:
            return c
        count += 1
    return ""

def main():
    s = input("Enter the string: ")
    k = int(input("Enter the value of K: "))
    result = get_next_day(s)
    print(get_kth_char(result, k))

if __name__ == '__main__':
    main()

