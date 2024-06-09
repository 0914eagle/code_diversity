
def f1(N, K, B, M, arr):
    # Calculate the hash of all non-empty subsequences
    hashes = []
    for i in range(1, N+1):
        for j in range(0, N-i+1):
            hashes.append(calculate_hash(arr[j:j+i], B, M))
    
    # Sort the hashes lexicographically
    hashes.sort()
    
    # Return the first K hashes
    return hashes[:K]

def calculate_hash(arr, B, M):
    # Calculate the hash of the array
    hash = 0
    for i in range(len(arr)):
        hash = (hash * B + arr[i]) % M
    return hash

if __name__ == '__main__':
    N, K, B, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*f1(N, K, B, M, arr))

