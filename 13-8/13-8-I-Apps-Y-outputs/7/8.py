
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def compute_product(A):
    product = 1
    for i in range(len(A)):
        product *= A[i]
    return product

def solve(N, A):
    product = compute_product(A)
    if product <= 10**18:
        return str(product)
    else:
        return "-1"

if __name__ == '__main__':
    N, A = read_input()
    print(solve(N, A))

