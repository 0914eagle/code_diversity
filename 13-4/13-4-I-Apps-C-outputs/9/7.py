
def get_polynomial(p, k):
    if p >= k:
        return [-1]
    
    d = 1
    while p % k != 0:
        p *= k
        d += 1
    
    coeffs = [p // k]
    for i in range(d - 1):
        coeffs.append(coeffs[i] // k)
    
    return coeffs

def main():
    p, k = map(int, input().split())
    coeffs = get_polynomial(p, k)
    if coeffs[0] == -1:
        print(coeffs[0])
    else:
        print(len(coeffs))
        print(*coeffs)

if __name__ == '__main__':
    main()

