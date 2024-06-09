
def get_smallest_k(arr, k):
    return sorted(arr)[:k]

def get_largest_k(arr, k):
    return sorted(arr, reverse=True)[:k]

def get_satisfying_integers(a, b, k):
    integers = list(range(a, b+1))
    smallest_k = get_smallest_k(integers, k)
    largest_k = get_largest_k(integers, k)
    return smallest_k + largest_k

if __name__ == '__main__':
    a, b, k = map(int, input().split())
    print(*get_satisfying_integers(a, b, k))

