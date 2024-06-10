
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
    
    # find the optimal subsequence for the left half
    left = get_optimal_subsequence(arr[:n//2], k)
    # find the optimal subsequence for the right half
    right = get_optimal_subsequence(arr[n//2:], k)
    
    # compare the two halves and return the better one
    if sum(left) < sum(right):
        return left
    else:
        return right

def solve(arr, k):
    # find the optimal subsequence of length k
    subsequence = get_optimal_subsequence(arr, k)
    # find the minimum and maximum elements in the subsequence
    min_element = min(subsequence)
    max_element = max(subsequence)
    # return the difference between the maximum and minimum elements
    return max_element - min_element

if __name__ == '__main__':
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, k))

