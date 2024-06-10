
def get_minutes(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return 0
    else:
        return 1 + max(a, b, c)

def main():
    a, b, c = map(int, input().split())
    print(get_minutes(a, b, c))

if __name__ == '__main__':
    main()

