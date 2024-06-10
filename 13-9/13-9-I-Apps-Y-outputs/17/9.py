
def get_digits(n):
    return len(str(n))

def get_largest_integer(a, b, x):
    for i in range(10**9):
        if a*i + b*get_digits(i) <= x:
            return i
    return 0

if __name__ == '__main__':
    a, b, x = map(int, input().split())
    print(get_largest_integer(a, b, x))

