
t = int(input())

for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    
    segments.sort(key=lambda x: (x[1], -x[0]))
    
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if segments[j][0] <= segments[i][0] and segments[i][1] <= segments[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))
