
def f1(N, K, B, M):
    # function to calculate the hash of a subsequence
    def hash_subsequence(subsequence):
        hash_value = 0
        for i in range(len(subsequence)):
            hash_value += subsequence[i] * B ** (len(subsequence) - i - 1)
        return hash_value % M
    
    # function to calculate all hash values of non-empty subsequences
    def calculate_hash_values(arr):
        hash_values = []
        for i in range(1, len(arr) + 1):
            for subsequence in itertools.combinations(arr, i):
                hash_values.append(hash_subsequence(subsequence))
        return hash_values
    
    # calculate all hash values and return the first K elements
    return calculate_hash_values(arr)[:K]

def f2(...):
    ...

if __name__ == '__main__':
    N, K, B, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*f1(N, K, B, M), sep='\n')

