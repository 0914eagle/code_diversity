
def get_input():
    return map(int, input().split())

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 == 1

def solve():
    a, b = get_input()
    product = a * b
    if is_even(product):
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    print(solve())

