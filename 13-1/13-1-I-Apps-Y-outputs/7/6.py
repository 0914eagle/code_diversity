
def f1(x, a, b):
    if b <= x:
        return "delicious"
    elif b > x + 1:
        return "dangerous"
    else:
        return "safe"

def f2(...):
    ...

if __name__ == '__main__':
    x, a, b = map(int, input().split())
    print(f1(x, a, b))

