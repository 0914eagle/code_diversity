
def get_permutation(b_prime, c_prime):
    n = len(b_prime) + 1
    a = [0] * n
    for i in range(n):
        a[i] = b_prime[i]
    for i in range(n):
        if a[i] > c_prime[i]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

def get_array(a, p):
    n = len(a)
    b = [0] * (n-1)
    c = [0] * (n-1)
    for i in range(n-1):
        b[i] = min(a[i], a[i+1])
        c[i] = max(a[i], a[i+1])
    b_prime = [0] * (n-1)
    c_prime = [0] * (n-1)
    for i in range(n-1):
        b_prime[i] = b[p[i]-1]
        c_prime[i] = c[p[i]-1]
    return b_prime, c_prime

def main():
    b_prime = list(map(int, input().split()))
    c_prime = list(map(int, input().split()))
    a = get_permutation(b_prime, c_prime)
    if a == -1:
        print(-1)
    else:
        print(*a)

if __name__ == '__main__':
    main()

