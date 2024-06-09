
def get_input():
    return list(map(int, input().split()))

def find_max_product(a, b, c, d):
    max_product = 0
    for x in range(a, b+1):
        for y in range(c, d+1):
            product = x * y
            if product > max_product:
                max_product = product
    return max_product

if __name__ == '__main__':
    a, b, c, d = get_input()
    print(find_max_product(a, b, c, d))

