
import itertools

def get_subsequences(arr):
    return [list(subsequence) for subsequence in itertools.chain.from_iterable(itertools.combinations(arr, r) for r in range(1, len(arr)+1))]

def get_hash(subsequence, B, M):
    hash_value = 0
    for i, element in enumerate(subsequence):
        hash_value += element * B**(len(subsequence) - i - 1)
    return hash_value % M

def get_hashes(arr, K, B, M):
    subsequences = get_subsequences(arr)
    return [get_hash(subsequence, B, M) for subsequence in sorted(subsequences)[:K]]

def main():
    N, K, B, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*get_hashes(arr, K, B, M), sep='\n')

if __name__ == '__main__':
    main()

