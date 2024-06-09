
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
    # if the maximum and minimum elements are not adjacent, we can swap them and get a better answer
    if abs(max_index - min_index) > 1:
        a[max_index], a[min_index] = a[min_index], a[max_index]
        return solve(a, k-1)
    # if the maximum and minimum elements are adjacent, we can increase or decrease the element in between them and get a better answer
    if max_index > min_index:
        for i in range(min_index+1, max_index):
            a[i] += 1
            ans = solve(a, k-1)
            if ans < abs(max(a) - min(a)):
                return ans
            a[i] -= 1
    if min_index > max_index:
        for i in range(max_index+1, min_index):
            a[i] -= 1
            ans = solve(a, k-1)
            if ans < abs(max(a) - min(a)):
                return ans
            a[i] += 1
    return abs(max(a) - min(a))

