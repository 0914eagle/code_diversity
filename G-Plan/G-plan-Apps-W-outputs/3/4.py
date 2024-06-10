
def split_bacteria(n):
    nights = 0
    splits = []
    
    while n > 1:
        if n % 2 == 0:
            splits.append(0)
        else:
            splits.append(1)
            n -= 1
        n //= 2
        nights += 1
    
    if n == 1:
        splits.append(0)
        nights += 1
    
    return nights, splits[::-1]

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nights, splits = split_bacteria(n)
        
        if nights > 100:
            print(-1)
        else:
            print(nights)
            print(*splits)
