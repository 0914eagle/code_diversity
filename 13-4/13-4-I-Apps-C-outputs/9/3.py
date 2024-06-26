
def f1(p, k):
    if p >= k:
        return -1
    
    d = 1
    a = [p]
    while a[-1] % k != 0:
        a.append(a[-1] * 10 % k)
        d += 1
    
    return d, a

def f2(p, k):
    if p >= k:
        return -1
    
    d = 1
    a = [p]
    while a[-1] % k != 0:
        a.append(a[-1] * 10 % k)
        d += 1
    
    return d, a

if __name__ == '__main__':
    p, k = map(int, input().split())
    d, a = f1(p, k)
    print(d)
    print(*a)

