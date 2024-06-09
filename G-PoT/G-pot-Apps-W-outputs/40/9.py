
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_reach_target_time(target_time):
    i, j, cancel_count = 0, 0, 0
    while i < n and j < m:
        if a[i] + t_a <= b[j]:
            if b[j] + t_b <= target_time:
                j += 1
            else:
                cancel_count += 1
                if cancel_count > k:
                    return False
                j += 1
        else:
            i += 1
    return j == m

left, right = max(a[0], b[0]), a[-1] + t_a + t_b
result = -1

while left <= right:
    mid = (left + right) // 2
    if can_reach_target_time(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
