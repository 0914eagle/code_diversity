
def is_possible(a, b, c):
    return a + b == c or a + c == b or b + c == a

def main():
    a, b, c = map(int, input().split())
    print("Yes" if is_possible(a, b, c) else "No")

if __name__ == '__main__':
    main()

