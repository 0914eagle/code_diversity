
def get_lexicographically_smaller(a, b):
    str_a = a * b
    str_b = b * a
    if str_a < str_b:
        return str_a
    else:
        return str_b

def main():
    a, b = map(int, input().split())
    print(get_lexicographically_smaller(a, b))

if __name__ == '__main__':
    main()

