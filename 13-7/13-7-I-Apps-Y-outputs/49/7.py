
def is_between(a, b, c):
    return a <= c <= b

def main():
    a, b, c = map(int, input().split())
    if is_between(a, b, c):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

