
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Find the smallest multiple of a that is less than or equal to b
    B = (b // a) * a
    
    # Find the smallest multiple of B that is less than or equal to c
    C = (c // B) * B
    
    # Calculate the number of operations needed to reach A, B, C
    operations = abs(a - A) + abs(b - B) + abs(c - C)
    
    print(operations)
    print(a, B, C)
