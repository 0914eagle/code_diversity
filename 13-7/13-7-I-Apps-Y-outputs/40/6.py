
def lexicographically_smaller(a, b):
    if a == b:
        return a
    else:
        return "3" * b + "4" * a

def main():
    a, b = map(int, input().split())
    print(lexicographically_smaller(a, b))

if __name__ == '__main__':
    main()

