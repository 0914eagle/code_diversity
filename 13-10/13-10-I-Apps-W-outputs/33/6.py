
def get_product_pairs(numbers):
    n = len(numbers)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append(numbers[i] * numbers[j])
    return sorted(pairs)

def kth_number(n, k, numbers):
    products = get_product_pairs(numbers)
    return products[k-1]

if __name__ == '__main__':
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(kth_number(n, k, numbers))

