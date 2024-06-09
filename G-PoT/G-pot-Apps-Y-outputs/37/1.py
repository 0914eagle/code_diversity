
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Find the minimum number of operations needed
    operations = max(0, 2 * (b - a) + max(0, 2 * (c - b) - 1))
    
    # Find suitable values for A, B, C
    A = a
    B = a
    C = a
    while B % A != 0 or C % B != 0:
        if B % A != 0:
            B += 1
            operations += 1
        if C % B != 0:
            C += 1
            operations += 1
    
    print(operations)
    print(A, B, C)
