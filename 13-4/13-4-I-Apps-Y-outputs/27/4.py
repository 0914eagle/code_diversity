
def get_input():
    return list(map(int, input().split()))

def get_smallest_k(arr, k):
    return sorted(arr)[:k]

def get_largest_k(arr, k):
    return sorted(arr, reverse=True)[:k]

def get_result(arr, k):
    smallest_k = get_smallest_k(arr, k)
    largest_k = get_largest_k(arr, k)
    return sorted(set(smallest_k + largest_k))

def main():
    A, B, K = get_input()
    result = get_result(range(A, B+1), K)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()

