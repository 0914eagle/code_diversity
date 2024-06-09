
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Find the closest divisible numbers
    A = a
    B = b + (a - b % a) % a
    C = c + (b - c % b) % b
    
    # Calculate the number of operations needed
    operations = abs(b - B) // 2 + abs(c - C) // 2
    
    print(operations)
    print(A, B, C)
