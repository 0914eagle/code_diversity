
def get_input():
    return list(map(int, input().split()))

def get_k_smallest(arr, k):
    return sorted(arr)[:k]

def get_k_largest(arr, k):
    return sorted(arr, reverse=True)[:k]

def solve(a, b, k):
    arr = list(range(a, b+1))
    return list(set(get_k_smallest(arr, k) + get_k_largest(arr, k)))

if __name__ == '__main__':
    a, b, k = get_input()
    print(*solve(a, b, k))

