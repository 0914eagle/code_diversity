
def input_data():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def compute_product(N, A):
    product = 1
    for i in range(N):
        product *= A[i]
    return product

def print_result(result):
    if result > 10**18:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    N, A = input_data()
    result = compute_product(N, A)
    print_result(result)

