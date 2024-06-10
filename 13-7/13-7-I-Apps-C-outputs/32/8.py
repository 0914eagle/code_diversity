
def get_subsequences(arr):
    subsequences = []
    for i in range(len(arr)):
        for subsequence in get_subsequences(arr[i+1:]):
            subsequences.append([arr[i]] + subsequence)
    if not arr:
        subsequences.append([])
    return subsequences

def get_hash(arr, base, mod):
    hash_value = 0
    for i in range(len(arr)):
        hash_value += arr[i] * base ** (len(arr) - i - 1)
    return hash_value % mod

def get_hashes(arr, base, mod, k):
    subsequences = get_subsequences(arr)
    return [get_hash(subsequence, base, mod) for subsequence in subsequences[:k]]

def main():
    n, k, base, mod = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*get_hashes(arr, base, mod, k), sep='\n')

if __name__ == '__main__':
    main()

