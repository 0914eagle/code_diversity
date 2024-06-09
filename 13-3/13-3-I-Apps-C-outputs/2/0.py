
def f1(a):
    return (a * 2) - 2

def f2(a):
    return (a * (a + 1)) // 2

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(f1(a[0]))
    print(f2(a[1]))

