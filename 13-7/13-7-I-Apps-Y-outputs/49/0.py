
def is_between(a, b, c):
    return a <= c <= b

def main():
    a, b, c = map(int, input().split())
    print("Yes" if is_between(a, b, c) else "No")

if __name__ == '__main__':
    main()

