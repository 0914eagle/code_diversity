
def get_input():
    return list(map(int, input().split()))

def get_smallest_k(numbers, k):
    return sorted(numbers)[:k]

def get_largest_k(numbers, k):
    return sorted(numbers, reverse=True)[:k]

def get_satisfying_integers(a, b, k):
    integers = list(range(a, b+1))
    smallest_k = get_smallest_k(integers, k)
    largest_k = get_largest_k(integers, k)
    return sorted(set(smallest_k + largest_k))

def main():
    a, b, k = get_input()
    integers = get_satisfying_integers(a, b, k)
    print(*integers)

if __name__ == '__main__':
    main()

