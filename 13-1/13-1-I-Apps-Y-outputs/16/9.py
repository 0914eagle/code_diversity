
def is_even_or_odd(a, b):
    product = a * b
    if product % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(is_even_or_odd(a, b))

