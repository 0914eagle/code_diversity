
def get_permutation(b_prime, c_prime):
    n = len(b_prime) + 1
    a = [0] * n
    for i in range(n):
        a[i] = b_prime[i]
    for i in range(n):
        if a[i] > c_prime[i]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

def get_array(a):
    n = len(a)
    b = [0] * (n-1)
    c = [0] * (n-1)
    for i in range(n-1):
        b[i] = min(a[i], a[i+1])
        c[i] = max(a[i], a[i+1])
    return b, c

def main():
    n = int(input())
    b_prime = list(map(int, input().split()))
    c_prime = list(map(int, input().split()))
    a = get_permutation(b_prime, c_prime)
    b, c = get_array(a)
    if b == b_prime and c == c_prime:
        print(*a)
    else:
        print(-1)

if __name__ == '__main__':
    main()

