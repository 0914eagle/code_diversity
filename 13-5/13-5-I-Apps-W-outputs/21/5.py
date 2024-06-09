
def get_array_from_b_c(b, c):
    n = len(b) + 1
    a = [0] * n
    for i in range(n - 1):
        a[i] = min(b[i], c[i])
        a[i + 1] = max(b[i], c[i])
    return a

def get_permutation_from_b_c(b, c):
    n = len(b) + 1
    p = [0] * n
    for i in range(n - 1):
        p[i] = b.index(min(b[i], c[i]))
    return p

def main():
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a = get_array_from_b_c(b, c)
    p = get_permutation_from_b_c(b, c)
    if a == [] or p == []:
        print(-1)
    else:
        print(*a)

if __name__ == '__main__':
    main()

