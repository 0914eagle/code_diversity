
def get_input():
    return list(map(int, input().split()))

def get_smallest_k(arr, k):
    return sorted(arr)[:k]

def get_largest_k(arr, k):
    return sorted(arr, reverse=True)[:k]

def get_solution(arr, k):
    smallest_k = get_smallest_k(arr, k)
    largest_k = get_largest_k(arr, k)
    return sorted(set(smallest_k + largest_k))

def main():
    a, b, k = get_input()
    print(*get_solution(range(a, b+1), k))

if __name__ == '__main__':
    main()

