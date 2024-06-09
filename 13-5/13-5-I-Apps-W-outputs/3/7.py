
def get_input():
    return list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(a1, b1, a2, b2, L, R):
    g = gcd(a1, a2)
    a1 //= g
    a2 //= g
    b1 //= g
    b2 //= g
    count = 0
    for k in range((R - L) // a1 + 1):
        x = a1 * k + b1
        if L <= x <= R:
            count += 1
    for l in range((R - L) // a2 + 1):
        x = a2 * l + b2
        if L <= x <= R and x % a1 == 0:
            count -= 1
    return count

if __name__ == '__main__':
    a1, b1, a2, b2, L, R = get_input()
    print(solve(a1, b1, a2, b2, L, R))

