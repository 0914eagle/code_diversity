
def f1(X, A):
    if X < A:
        return 0
    else:
        return 10

def f2(...):
    ...

if __name__ == '__main__':
    X, A = map(int, input().split())
    print(f1(X, A))

