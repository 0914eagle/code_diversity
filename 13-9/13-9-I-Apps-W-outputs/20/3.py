
def k_rounding(n, k):
    if n == 0:
        return 0
    if k == 0:
        return n
    
    x = 1
    while x < n:
        x *= 10
    
    while x % n != 0:
        x //= 10
    
    while x % 10 != 0:
        x *= 10
    
    return x

def main():
    n, k = map(int, input().split())
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

