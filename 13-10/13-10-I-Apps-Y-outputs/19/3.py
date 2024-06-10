
def get_string_list(s, t):
    string_list = []
    for i in range(ord(s), ord(t) + 1):
        string_list.append(chr(i))
    return string_list

def get_median(string_list):
    return string_list[len(string_list) // 2]

def main():
    k = int(input())
    s = input()
    t = input()
    string_list = get_string_list(s, t)
    print(get_median(string_list))

if __name__ == '__main__':
    main()

