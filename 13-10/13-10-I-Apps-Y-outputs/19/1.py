
def get_list_of_strings(s, t, k):
    
    list_of_strings = []
    for i in range(ord(s[0]), ord(t[0]) + 1):
        list_of_strings.append(chr(i) + s[1:])
    for i in range(ord(s[0]), ord(t[0]) + 1):
        list_of_strings.append(chr(i) + t[1:])
    return sorted(list_of_strings)

def get_median(list_of_strings):
    
    return list_of_strings[len(list_of_strings) // 2]

def main():
    k = int(input())
    s = input()
    t = input()
    list_of_strings = get_list_of_strings(s, t, k)
    print(get_median(list_of_strings))

if __name__ == '__main__':
    main()

