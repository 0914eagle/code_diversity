
def get_sorted_products(numbers):
    products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            products.append(numbers[i] * numbers[j])
    products.sort()
    return products

def solve(N, K, numbers):
    products = get_sorted_products(numbers)
    return products[K-1]

if __name__ == '__main__':
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solve(N, K, numbers))

