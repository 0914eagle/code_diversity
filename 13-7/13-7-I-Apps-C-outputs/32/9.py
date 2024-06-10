
def get_subsequences(arr):
    subsequences = []
    for i in range(len(arr)):
        for subsequence in get_subsequences(arr[i+1:]):
            subsequences.append([arr[i]] + subsequence)
    if not arr:
        subsequences.append([])
    return subsequences

def lexicographically_smaller(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return arr1[i] < arr2[i]
    return len(arr1) < len(arr2)

def get_hash(arr, b, m):
    hash_value = 0
    for i in range(len(arr)):
        hash_value = (hash_value * b + arr[i]) % m
    return hash_value

def get_hashes(arr, k, b, m):
    subsequences = get_subsequences(arr)
    hashes = []
    for i in range(k):
        hashes.append(get_hash(subsequences[i], b, m))
    return hashes

def main():
    n, k, b, m = map(int, input().split())
    arr = list(map(int, input().split()))
    hashes = get_hashes(arr, k, b, m)
    for hash in hashes:
        print(hash)

if __name__ == '__main__':
    main()

