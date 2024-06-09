
def f1(b, c):
    # Function to reconstruct array a and permutation p from arrays b and c
    # b and c are arrays of length n-1
    n = len(b) + 1
    a = [0] * n
    p = [0] * n
    for i in range(n-1):
        a[i] = min(b[i], c[i])
        a[i+1] = max(b[i], c[i])
        p[i] = i + 1
    return a, p

def f2(b, c):
    # Function to check if arrays b and c are valid
    # b and c are arrays of length n-1
    n = len(b) + 1
    for i in range(n-1):
        if b[i] > c[i]:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    if f2(b, c):
        a, p = f1(b, c)
        print(*a)
    else:
        print(-1)

