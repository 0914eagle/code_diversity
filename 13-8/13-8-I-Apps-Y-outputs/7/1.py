
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def compute_product(A):
    product = 1
    for a in A:
        product *= a
    return product

def check_product(product):
    if product > 10**18:
        return -1
    else:
        return product

def main():
    N, A = read_input()
    product = compute_product(A)
    result = check_product(product)
    print(result)

if __name__ == '__main__':
    main()

