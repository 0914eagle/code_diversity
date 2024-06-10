
def add_integers(a, b):
    return a + b

def main():
    a, b = map(int, input().split())
    print(add_integers(a, b))

if __name__ == '__main__':
    main()

