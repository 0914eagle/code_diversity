
def get_input():
    return list(map(int, input().split()))

def get_k_smallest(arr, k):
    return sorted(arr)[:k]

def get_k_largest(arr, k):
    return sorted(arr, reverse=True)[:k]

def get_solution(arr, k):
    return list(set(get_k_smallest(arr, k) + get_k_largest(arr, k)))

def main():
    a, b, k = get_input()
    solution = get_solution(range(a, b+1), k)
    print(*solution)

if __name__ == '__main__':
    main()

