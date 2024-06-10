
def read_input():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, A

def get_pairs(A):
    return [(a, b) for a in A for b in A if a != b]

def get_products(pairs):
    return [a * b for a, b in pairs]

def solve(N, K, A):
    pairs = get_pairs(A)
    products = get_products(pairs)
    products.sort()
    return products[K - 1]

def main():
    N, K, A = read_input()
    print(solve(N, K, A))

if __name__ == '__main__':
    main()

