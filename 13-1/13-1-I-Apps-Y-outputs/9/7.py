
def f1(a, b, c):
    return a, b, c

def f2(a, b, c):
    return a, c, b

def f3(a, b, c):
    return b, a, c

def f4(a, b, c):
    return b, c, a

def f5(a, b, c):
    return c, a, b

def f6(a, b, c):
    return c, b, a

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    order = input()
    if order == 'ABC':
        print(*f1(a, b, c))
    elif order == 'ACB':
        print(*f2(a, b, c))
    elif order == 'BAC':
        print(*f3(a, b, c))
    elif order == 'BCA':
        print(*f4(a, b, c))
    elif order == 'CAB':
        print(*f5(a, b, c))
    elif order == 'CBA':
        print(*f6(a, b, c))

