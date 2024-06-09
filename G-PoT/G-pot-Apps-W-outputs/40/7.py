
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_reach_C(time):
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
    return cnt

low = 0
high = 10**18
while low < high:
    mid = (low + high) // 2
    if can_reach_C(mid) <= k:
        high = mid
    else:
        low = mid + 1

if can_reach_C(low) <= k:
    print(low + t_a + t_b)
else:
    print(-1)
