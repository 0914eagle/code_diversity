
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 == 1

def solve(a, b):
    product = a * b
    if is_even(product):
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solve(a, b))

