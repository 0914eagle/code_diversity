
def lexicographically_smaller(a, b):
    a_str = a * b
    b_str = b * a
    if a_str < b_str:
        return a_str
    else:
        return b_str

def main():
    a, b = map(int, input().split())
    print(lexicographically_smaller(a, b))

if __name__ == '__main__':
    main()

