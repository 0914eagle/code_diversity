
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check_time(t):
    cnt = 0
    j = 0
    for i in range(n):
        while j < m and b[j] < a[i] + t_a:
            j += 1
        if j == m:
            break
        if b[j] >= a[i] + t_a:
            cnt += 1
            j += 1
        if cnt > k:
            return False
    return cnt <= k

left = 0
right = 10**18
while left < right:
    mid = (left + right) // 2
    if check_time(mid):
        right = mid
    else:
        left = mid + 1

if left == 10**18:
    print(-1)
else:
    print(left + t_a + t_b)
