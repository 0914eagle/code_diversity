
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Find the closest multiple of a to b
    b_new = (b // a) * a
    if b % a > a // 2:
        b_new += a
    
    # Find the closest multiple of b to c
    c_new = (c // b_new) * b_new
    if c % b_new > b_new // 2:
        c_new += b_new
    
    operations = abs(b - b_new) + abs(c - c_new)
    
    print(operations)
    print(a, b_new, c_new)
