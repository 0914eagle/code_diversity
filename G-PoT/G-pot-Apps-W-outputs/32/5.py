
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Find a subset with zero sum
    subset = []
    for i in range(n):
        if a[i] == 0:
            subset = [i+1]
            break
    if not subset:
        for i in range(n):
            if a[i] + a[(i+1)%n] == 0:
                subset = [i+1, (i+1)%n+1]
                break
    
    # Output the subset
    print(len(subset))
    print(*subset)
