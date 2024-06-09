
def solve(a, k):
    n = len(a)
    if k == 0:
        return 0
    if n == 1:
        return 0
    if k == 1:
        return abs(max(a) - min(a))
    # find the index of the maximum and minimum elements
    max_index = a.index(max(a))
    min_index = a.index(min(a))
    # if the maximum and minimum elements are not at the edges,
    # we can increase or decrease them by 1 and get a better answer
    if max_index != 0 and max_index != n-1:
        a[max_index] += 1
        a[min_index] -= 1
        return solve(a, k-1)
    # if the maximum element is at the edge, we can only decrease the minimum element
    elif max_index == 0:
        a[min_index] -= 1
        return solve(a, k-1)
    # if the minimum element is at the edge, we can only increase the maximum element
    else:
        a[max_index] += 1
        return solve(a, k-1)

