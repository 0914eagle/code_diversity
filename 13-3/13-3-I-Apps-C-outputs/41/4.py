
def f1(N, K, B, M, arr):
    # Calculate the hash of all non-empty subsequences
    subseqs = []
    for i in range(1, 2**N):
        subseq = []
        for j in range(N):
            if i & (1 << j):
                subseq.append(arr[j])
        subseqs.append(subseq)
    
    # Sort the subsequence lexicographically
    subseqs.sort(key=lambda x: (x[0], x[1:]))
    
    # Calculate the hash of the first K subsequence
    result = []
    for i in range(K):
        h = 0
        for j in range(len(subseqs[i])):
            h = (h * B + subseqs[i][j]) % M
        result.append(h)
    
    return result

def f2(...):
    ...

if __name__ == '__main__':
    N, K, B, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = f1(N, K, B, M, arr)
    for i in result:
        print(i)

