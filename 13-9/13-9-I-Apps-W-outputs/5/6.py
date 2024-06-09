
def solve(n, l, lanterns):
    lanterns = sorted(lanterns)
    left = 0
    right = l
    while left < right:
        mid = (left + right) // 2
        if is_lit(lanterns, mid):
            right = mid
        else:
            left = mid + 1
    return left

def is_lit(lanterns, d):
    for i in range(len(lanterns) - 1):
        if lanterns[i + 1] - lanterns[i] > d * 2:
            return False
    return True

l, n = map(int, input().split())
lanterns = list(map(int, input().split()))
print(solve(n, l, lanterns))

