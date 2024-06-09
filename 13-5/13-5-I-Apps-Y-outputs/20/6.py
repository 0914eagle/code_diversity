
def is_possible(a, b, c):
    return a + b == c or a + c == b or b + c == a

def main():
    a, b, c = map(int, input().split())
    if is_possible(a, b, c):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

