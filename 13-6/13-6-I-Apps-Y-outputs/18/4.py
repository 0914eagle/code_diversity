
def is_even(a, b):
    product = a * b
    if product % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    a, b = map(int, input().split())
    print(is_even(a, b))

if __name__ == '__main__':
    main()

