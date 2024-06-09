
def solve(a, k):
    n = len(a)
    if n == 1:
        return 0
    if k == 0:
        return abs(max(a) - min(a))
    # find the index of the maximum and minimum elements
    max_index = a.index(max(a))
    min_index = a.index(min(a))
    # if the maximum and minimum elements are not adjacent, we can swap them and get a better answer
    if abs(max_index - min_index) > 1:
        a[max_index], a[min_index] = a[min_index], a[max_index]
        k -= 1
    # if the maximum element is not at the end of the array, we can move it to the end and get a better answer
    if max_index < n-1:
        a[max_index], a[n-1] = a[n-1], a[max_index]
        k -= 1
    # if the minimum element is not at the start of the array, we can move it to the start and get a better answer
    if min_index > 0:
        a[min_index], a[0] = a[0], a[min_index]
        k -= 1
    return solve(a, k)

