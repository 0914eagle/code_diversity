
def split_bacteria(n):
    nights = 0
    splits = []
    
    while n > 1:
        if n % 2 == 0:
            splits.append(n // 2)
            n //= 2
        else:
            splits.append(n // 2 + 1)
            n = n // 2 + 1
        nights += 1
    
    return nights, splits

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nights, splits = split_bacteria(n)
        
        if nights == 0:
            print(-1)
        else:
            print(nights)
            print(" ".join(map(str, splits)))
