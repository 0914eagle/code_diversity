
def f(a):
    return len(set(a))

def f1(n, a):
    return f(a)

def f2(n, a):
    return f(a)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

