
def get_input():
    return input().split()

def get_lexicographically_smaller(a, b):
    if a == b:
        return a
    else:
        return '3' * int(b) if int(a) > int(b) else '4' * int(a)

def main():
    a, b = get_input()
    print(get_lexicographically_smaller(a, b))

if __name__ == '__main__':
    main()

