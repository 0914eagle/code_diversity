
def get_input():
    return list(map(int, input().split()))

def compute_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def check_overflow(product):
    return product <= 10**18

def main():
    numbers = get_input()
    product = compute_product(numbers)
    if check_overflow(product):
        print(product)
    else:
        print(-1)

if __name__ == '__main__':
    main()

