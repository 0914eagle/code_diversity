
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def compute_product(A):
    product = 1
    for i in range(len(A)):
        product *= A[i]
    return product

def check_overflow(product):
    return product <= 10**18

def main():
    N, A = read_input()
    product = compute_product(A)
    if check_overflow(product):
        print(product)
    else:
        print(-1)

if __name__ == '__main__':
    main()

