
def get_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

def solve(numbers):
    product = get_product(numbers)
    if product > 10**18:
        return -1
    return product

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(solve(numbers))

if __name__ == '__main__':
    main()

