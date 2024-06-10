
def get_strings(a_00, a_01, a_10, a_11):
    strings = []
    for i in range(a_00):
        strings.append("00")
    for i in range(a_01):
        strings.append("01")
    for i in range(a_10):
        strings.append("10")
    for i in range(a_11):
        strings.append("11")
    return strings

def check_strings(strings, a_00, a_01, a_10, a_11):
    for string in strings:
        if string.count("00") == a_00 and string.count("01") == a_01 and string.count("10") == a_10 and string.count("11") == a_11:
            return string
    return "Impossible"

def main():
    a_00, a_01, a_10, a_11 = map(int, input().split())
    strings = get_strings(a_00, a_01, a_10, a_11)
    result = check_strings(strings, a_00, a_01, a_10, a_11)
    print(result)

if __name__ == '__main__':
    main()

