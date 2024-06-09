
def f1(b, c):
    # Function to recover the array a and permutation p from the arrays b and c
    # b and c are lists of integers
    n = len(b) + 1
    a = [0] * n
    p = [0] * n
    for i in range(n):
        a[i] = b[i]
        p[i] = i
    for i in range(n-1):
        for j in range(i+1, n):
            if b[i] > b[j] and c[i] < c[j]:
                a[i], a[j] = a[j], a[i]
                p[i], p[j] = p[j], p[i]
    return a, p

def f2(b, c):
    # Function to check if the arrays b and c are valid
    # b and c are lists of integers
    n = len(b) + 1
    for i in range(n-1):
        for j in range(i+1, n):
            if b[i] > b[j] and c[i] < c[j]:
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    if f2(b, c):
        a, p = f1(b, c)
        print(*a)
    else:
        print(-1)

