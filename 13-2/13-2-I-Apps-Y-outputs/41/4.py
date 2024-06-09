
def f1(x, a):
    if x < a:
        return 0
    else:
        return 10

def f2(...):
    ...

if __name__ == '__main__':
    x, a = map(int, input().split())
    print(f1(x, a))

