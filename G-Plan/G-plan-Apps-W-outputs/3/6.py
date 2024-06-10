
def split_bacteria(n):
    if n % 2 != 0:
        return -1
    
    nights = 0
    splitting_pattern = []
    
    while n > 1:
        if n % 2 == 0:
            splitting_pattern.append(n // 2)
            n //= 2
        else:
            splitting_pattern.append((n // 2) - 1)
            n = (n // 2) + 1
        
        nights += 1
    
    return nights, splitting_pattern

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nights, splitting_pattern = split_bacteria(n)
        
        if nights == -1:
            print(-1)
        else:
            print(nights)
            print(*splitting_pattern)
