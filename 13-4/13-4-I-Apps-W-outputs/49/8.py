
def f1(n):
    return (n * (n + 1)) // 2

def f2(n):
    return f1(n) + 1

if __name__ == '__main__':
    n = int(input())
    print(f2(n))

