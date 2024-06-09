
def f1(N, M, Q):
    # Your code here
    return

def f2(d, x):
    # Your code here
    return

if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    for _ in range(Q):
        query = input().split()
        if query[0] == '0':
            f1(N, M, Q, query)
        else:
            d, x = map(int, query[1:])
            print(f2(d, x))

