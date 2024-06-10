
def get_input():
    return input().split()

def get_smaller_string(a, b):
    str_a = a * b
    str_b = b * a
    if str_a < str_b:
        return str_a
    else:
        return str_b

def main():
    a, b = get_input()
    print(get_smaller_string(int(a), int(b)))

if __name__ == '__main__':
    main()

