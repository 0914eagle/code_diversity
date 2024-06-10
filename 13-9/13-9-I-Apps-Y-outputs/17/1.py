
def get_digits(n):
    return len(str(n))

def get_largest_integer(a, b, x):
    for i in range(1, 10**9+1):
        if a*i + b*get_digits(i) <= x:
            return i
    return 0

def main():
    a, b, x = map(int, input().split())
    print(get_largest_integer(a, b, x))

if __name__ == '__main__':
    main()

