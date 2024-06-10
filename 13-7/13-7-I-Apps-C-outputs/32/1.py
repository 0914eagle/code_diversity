
import itertools

def get_subsequences(arr):
    return [list(subsequence) for subsequence in itertools.chain.from_iterable(itertools.combinations(arr, r) for r in range(1, len(arr)+1))]

def get_hash(subsequence, base, mod):
    return sum(v * base ** (len(subsequence) - i - 1) for i, v in enumerate(subsequence)) % mod

def solve(arr, base, mod, k):
    subsequences = get_subsequences(arr)
    return [get_hash(subsequence, base, mod) for subsequence in subsequences[:k]]

def main():
    n, k, base, mod = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*solve(arr, base, mod, k), sep='\n')

if __name__ == '__main__':
    main()

