
def read_input():
    return map(int, input().split())

def f1(x, a):
    if x < a:
        return 0
    else:
        return 10

def f2(x, a):
    return f1(x, a)

if __name__ == '__main__':
    x, a = read_input()
    print(f2(x, a))

