
def add_integers(a, b):
    return a + b

def get_input():
    return list(map(int, input().split()))

def main():
    a, b = get_input()
    print(add_integers(a, b))

if __name__ == '__main__':
    main()

