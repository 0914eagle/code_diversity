
def f1(n, m, k):
    # n: number of events
    # m: number of implications
    # k: number of events known to have occurred
    return n, m, k

def f2(n, m, k):
    # n: number of events
    # m: number of implications
    # k: number of events known to have occurred
    return n, m, k

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    print(f1(n, m, k))
    print(f2(n, m, k))

