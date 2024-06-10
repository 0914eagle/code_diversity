
def get_input():
    return input().split()

def get_lexicographically_smaller(a, b):
    a_str = a * b
    b_str = b * a
    if a_str < b_str:
        return a_str
    else:
        return b_str

def main():
    a, b = get_input()
    print(get_lexicographically_smaller(int(a), int(b)))

if __name__ == '__main__':
    main()

