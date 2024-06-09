
t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    strengths = list(map(int, input().split()))
    
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + (-1)**i * strengths[i]
    
    for _ in range(q):
        l, r = map(int, input().split())
        diff = strengths[l-1] - strengths[r-1]
        if (r - l) % 2 == 0:
            print(prefix_sum[l-1] + prefix_sum[n] - prefix_sum[r] + diff)
        else:
            print(prefix_sum[l-1] + prefix_sum[n] - prefix_sum[r] - diff)
    
    print(prefix_sum[n])
