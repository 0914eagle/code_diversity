
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def can_reach_c(arrival_time):
    i = 0
    j = 0
    cancel_count = 0
    
    while i < n and j < m:
        if a[i] < b[j] and b[j] >= a[i] + t_a:
            i += 1
        else:
            j += 1
            cancel_count += 1
        
        if cancel_count > k:
            return False
        
        if i == n:
            return True
    
    return False

low = 0
high = 10**18

while low < high:
    mid = (low + high) // 2
    if can_reach_c(mid):
        high = mid
    else:
        low = mid + 1

if low == 10**18:
    print(-1)
else:
    print(low)
