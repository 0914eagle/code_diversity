
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_reach_target_time(target_time):
    i = 0
    j = 0
    cancel_count = 0

    while i < n and j < m:
        if a[i] + t_a <= b[j]:
            i += 1
        else:
            j += 1
            cancel_count += 1

        if cancel_count > k:
            return False

    while j < m:
        if b[j] < target_time:
            j += 1
        else:
            return True

    return False

left = 1
right = 10**18
result = -1

while left <= right:
    mid = (left + right) // 2
    if can_reach_target_time(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
