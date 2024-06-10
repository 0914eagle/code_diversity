
def get_optimal_subsequence(arr, k):
    n = len(arr)
    if n == 0:
        return []
    if k == 0:
        return arr
    if k == 1:
        return [min(arr)]
    if k == n:
        return arr
    
    # find the minimum element in the first k elements
    min_val = min(arr[:k])
    # find the index of the minimum element
    min_idx = arr.index(min_val)
    # remove the minimum element from the array
    arr.pop(min_idx)
    # recurse for the rest of the array
    return [min_val] + get_optimal_subsequence(arr, k-1)

def solve(arr, k, q):
    n = len(arr)
    if n == 0 or k == 0 or q == 0:
        return 0
    
    # find the optimal subsequence of length k
    opt_subseq = get_optimal_subsequence(arr, k)
    # find the largest and smallest element in the optimal subsequence
    largest = max(opt_subseq)
    smallest = min(opt_subseq)
    # return the difference between the largest and smallest element
    return largest - smallest

if __name__ == '__main__':
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, k, q))

