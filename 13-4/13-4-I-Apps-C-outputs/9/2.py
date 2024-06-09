
def f1(p, k):
    if p < 0 or k < 2:
        return -1
    
    coeffs = []
    while p > 0:
        coeffs.append(p % k)
        p //= k
    
    if coeffs[-1] == 0:
        return -1
    
    return coeffs

def f2(p, k):
    if p < 0 or k < 2:
        return -1
    
    coeffs = []
    while p > 0:
        coeffs.append(p % k)
        p //= k
    
    if coeffs[-1] == 0:
        return -1
    
    return coeffs

if __name__ == '__main__':
    p, k = map(int, input().split())
    coeffs = f1(p, k)
    if coeffs == -1:
        print(-1)
    else:
        print(len(coeffs))
        print(*coeffs)

