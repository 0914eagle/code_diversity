
def get_subsequences(arr):
    subsequences = []
    for i in range(len(arr)):
        for subsequence in get_subsequences(arr[i+1:]):
            subsequences.append([arr[i]] + subsequence)
    if not arr:
        subsequences.append([])
    return subsequences

def get_hash(subsequence, B, M):
    hash_value = 0
    for i in range(len(subsequence)):
        hash_value += subsequence[i] * B ** (len(subsequence) - i - 1)
    return hash_value % M

def get_hashes(arr, K, B, M):
    subsequences = get_subsequences(arr)
    return [get_hash(subsequence, B, M) for subsequence in subsequences[:K]]

def main():
    N, K, B, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*get_hashes(arr, K, B, M), sep='\n')

if __name__ == '__main__':
    main()

