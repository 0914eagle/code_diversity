
def get_pairs(A):
    n = len(A)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append(A[i] * A[j])
    return pairs

def kth_smallest(pairs, k):
    return sorted(pairs)[k-1]

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    pairs = get_pairs(A)
    print(kth_smallest(pairs, k))

if __name__ == '__main__':
    main()

