
def get_input():
    return list(map(int, input().split()))

def get_lexicographically_smaller(a, b):
    if a == b:
        return str(a)
    else:
        return "3" * b + "4" * a

def main():
    a, b = get_input()
    print(get_lexicographically_smaller(a, b))

if __name__ == '__main__':
    main()

