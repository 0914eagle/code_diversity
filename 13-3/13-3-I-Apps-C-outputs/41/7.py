
def f1(N, K, B, M, arr):
    # Calculate the hash of all non-empty subsequences
    subseqs = []
    for i in range(1, 2**N):
        subseq = []
        for j in range(N):
            if i & (1 << j):
                subseq.append(arr[j])
        subseqs.append(subseq)
    
    # Calculate the hash of each subsequence
    hashes = []
    for subseq in subseqs:
        hash = 0
        for i in range(len(subseq)):
            hash += subseq[i] * B**(len(subseq) - i - 1)
        hashes.append(hash % M)
    
    # Return the hashes of the first K subseqs
    return hashes[:K]

def f2(...):
    ...

if __name__ == '__main__':
    N, K, B, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*f1(N, K, B, M, arr))

