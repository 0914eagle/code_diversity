
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_reach_target_time(target_time):
    i = 0
    j = 0
    cancel_count = 0

    while i < n and j < m:
        if a[i] < b[j] and a[i] + t_a <= target_time:
            i += 1
        elif a[i] >= b[j] and a[i] + t_a <= b[j] + t_b:
            i += 1
        else:
            j += 1
            cancel_count += 1

        if cancel_count > k:
            return False

    return i < n or (j < m and b[j] + t_b <= target_time)

low = max(a[0], b[0]) + t_a
high = a[-1] + t_a + t_b
result = -1

while low <= high:
    mid = (low + high) // 2
    if can_reach_target_time(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
