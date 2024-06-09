
def get_max_sum(a, k, x):
    n = len(a)
    if n < k or x == 0:
        return -1
    if k == 1:
        return sum(a[:x])
    if x == 1:
        return max(a)
    if x == n:
        return sum(a)
    # divide and conquer
    left = get_max_sum(a[:n//2], k, x//2)
    right = get_max_sum(a[n//2:], k, x-x//2)
    if left != -1 and right != -1:
        return left + right
    # greedy
    max_sum = 0
    for i in range(n-k+1):
        sum = 0
        for j in range(i, i+k):
            sum += a[j]
        if sum > max_sum:
            max_sum = sum
    return max_sum

