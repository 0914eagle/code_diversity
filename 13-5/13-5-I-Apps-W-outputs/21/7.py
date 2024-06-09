
def f1(b, c):
    # Function to reconstruct array a and permutation p from arrays b and c
    # b and c are lists of integers
    n = len(b) + 1
    a = [0] * n
    p = [0] * n
    for i in range(n):
        a[i] = b[i] if b[i] < c[i] else c[i]
        p[i] = b[i] if b[i] < c[i] else c[i]
    return a, p

def f2(b, c):
    # Function to check if arrays b and c are valid
    # b and c are lists of integers
    n = len(b) + 1
    for i in range(n):
        if b[i] < 1 or b[i] > n or c[i] < 1 or c[i] > n:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    if not f2(b, c):
        print(-1)
    else:
        a, p = f1(b, c)
        print(*a)

