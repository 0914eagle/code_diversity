
def get_polynomial(p, k):
    if p >= k:
        return -1
    
    d = 1
    a = [p]
    while a[-1] % k != 0:
        a.append(a[-1] // k)
        d += 1
    
    return d, a[:-1]

def main():
    p, k = map(int, input().split())
    result = get_polynomial(p, k)
    if result == -1:
        print(-1)
    else:
        d, a = result
        print(d)
        print(*a)

if __name__ == '__main__':
    main()

