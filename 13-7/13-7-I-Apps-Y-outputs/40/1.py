
def get_input():
    return input().split()

def get_lexicographically_smaller(a, b):
    str1 = a * b
    str2 = b * a
    if str1 < str2:
        return str1
    else:
        return str2

def main():
    a, b = get_input()
    print(get_lexicographically_smaller(a, b))

if __name__ == '__main__':
    main()

