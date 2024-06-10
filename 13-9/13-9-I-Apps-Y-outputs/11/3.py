
def get_monotonic_renumberings(a):
    n = len(a)
    b = [0] * n
    b[0] = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            b[i] = b[i-1]
        else:
            b[i] = b[i-1] + 1
    return b

def count_monotonic_renumberings(a):
    n = len(a)
    b = get_monotonic_renumberings(a)
    count = 1
    for i in range(1, n):
        if b[i] == b[i-1]:
            count *= 2
        else:
            count *= 2 - 1
    return count % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(count_monotonic_renumberings(a))

