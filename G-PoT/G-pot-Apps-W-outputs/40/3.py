
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_reach_target_time(target_time):
    cnt_cancelled = 0
    j = 0
    for i in range(n):
        while j < m and b[j] < a[i] + t_a:
            j += 1
        if j >= m or b[j] > target_time:
            cnt_cancelled += 1
            if cnt_cancelled > k:
                return False
        else:
            j += 1
    return True

left = max(a) + t_a
right = max(a) + t_a + t_b * k
result = -1

while left <= right:
    mid = (left + right) // 2
    if can_reach_target_time(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
