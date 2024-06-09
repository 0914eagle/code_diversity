
t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    strengths = list(map(int, input().split()))
    diffs = [strengths[i] - strengths[i+1] if i % 2 == 0 else strengths[i+1] - strengths[i] for i in range(n-1)]
    
    total_strength = sum(diffs)
    print(total_strength)
    
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        
        if l > 0:
            total_strength -= diffs[l-1]
            total_strength += strengths[r] - strengths[l-1]
            diffs[l-1] = strengths[r] - strengths[l-1]
        
        if r < n-1:
            total_strength -= diffs[r]
            total_strength += strengths[r+1] - strengths[l]
            diffs[r] = strengths[r+1] - strengths[l]
        
        print(total_strength)
