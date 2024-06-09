
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check_time(x):
    cnt = 0
    j = 0
    for i in range(n):
        while j < m and b[j] < a[i] + t_a:
            j += 1
        if j >= m or b[j] > x:
            cnt += 1
        else:
            j += 1
    return cnt

left = max(a) + t_a
right = max(a) + t_a + t_b * k
while left < right:
    mid = (left + right) // 2
    if check_time(mid) <= k:
        right = mid
    else:
        left = mid + 1

if check_time(left) <= k:
    print(left)
else:
    print(-1)
