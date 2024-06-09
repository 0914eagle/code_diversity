
def get_k_rounding(n, k):
    if k == 0:
        return n
    
    x = 1
    while x % n != 0:
        x *= 10
    
    while len(str(x)) <= k:
        x *= 10
    
    return x

def main():
    n, k = map(int, input().split())
    print(get_k_rounding(n, k))

if __name__ == '__main__':
    main()

