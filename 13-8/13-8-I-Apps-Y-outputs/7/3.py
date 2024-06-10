
def get_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def check_exceeds_limit(product):
    return product > 10**18

def get_result(numbers):
    product = get_product(numbers)
    if check_exceeds_limit(product):
        return -1
    else:
        return product

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    result = get_result(numbers)
    print(result)

