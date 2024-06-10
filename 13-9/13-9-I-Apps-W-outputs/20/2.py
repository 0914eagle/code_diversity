
def k_rounding(n, k):
    if k == 0:
        return n
    
    while n % 10 != 0:
        n *= 10
    
    while len(str(n)) <= k:
        n *= 10
    
    return n

def main():
    n, k = map(int, input().split())
    print(k_rounding(n, k))

if __name__ == '__main__':
    main()

