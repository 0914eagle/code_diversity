
def get_array_a(b_prime, c_prime):
    n = len(b_prime) + 1
    a = [0] * n
    for i in range(n):
        a[i] = b_prime[i] + c_prime[i]
    return a

def get_permutation_p(b_prime, c_prime):
    n = len(b_prime) + 1
    p = [0] * n
    for i in range(n):
        p[i] = i + 1
    return p

def main():
    n = int(input())
    b_prime = list(map(int, input().split()))
    c_prime = list(map(int, input().split()))
    a = get_array_a(b_prime, c_prime)
    p = get_permutation_p(b_prime, c_prime)
    print(*a)

if __name__ == '__main__':
    main()

