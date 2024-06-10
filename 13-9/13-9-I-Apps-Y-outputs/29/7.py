
def input_data():
    n = int(input())
    q = list(map(int, input().split()))
    return n, q

def is_permutation(q, n):
    if len(q) != n-1:
        return False
    for i in range(n-1):
        if q[i] < 0 or q[i] > n-1:
            return False
    return True

def get_permutation(q, n):
    p = [0] * n
    p[0] = 1
    for i in range(n-1):
        p[i+1] = p[i] + q[i]
    return p

def main():
    n, q = input_data()
    if not is_permutation(q, n):
        print(-1)
    else:
        p = get_permutation(q, n)
        print(*p)

if __name__ == '__main__':
    main()

