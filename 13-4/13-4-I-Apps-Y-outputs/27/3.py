
def get_input():
    return list(map(int, input().split()))

def get_k_smallest(arr, k):
    return sorted(arr)[:k]

def get_k_largest(arr, k):
    return sorted(arr, reverse=True)[:k]

def solve(A, B, K):
    arr = list(range(A, B+1))
    k_smallest = get_k_smallest(arr, K)
    k_largest = get_k_largest(arr, K)
    return list(set(k_smallest + k_largest))

if __name__ == '__main__':
    A, B, K = get_input()
    print(*solve(A, B, K))

