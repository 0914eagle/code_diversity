
def f1(n, a):
    # find the number of pairs (i, j) such that i < j and a[i] & a[j] >= a[i] ^ a[j]
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] & a[j] >= a[i] ^ a[j]:
                count += 1
    return count

def f2(n, a):
    # find the number of pairs (i, j) such that i < j and a[i] & a[j] >= a[i] ^ a[j]
    # using bitwise operations
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] & a[j] >= a[i] ^ a[j]:
                count += 1
    return count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(f1(n, a))
        print(f2(n, a))

