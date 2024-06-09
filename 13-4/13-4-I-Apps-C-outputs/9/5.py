
def get_polynomial(p, k):
    if p >= k:
        return -1
    
    d = 1
    while p % k != 0:
        p *= k
        d += 1
    
    a = [0] * d
    a[d-1] = 1
    return d, a

def main():
    p, k = map(int, input().split())
    d, a = get_polynomial(p, k)
    if d == -1:
        print(-1)
    else:
        print(d)
        for i in range(d):
            print(a[i], end=" ")
        print()

if __name__ == '__main__':
    main()

