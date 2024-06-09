
def f1(n):
    return n % 2

def f2(n):
    return (n // 2) % 2

if __name__ == '__main__':
    n = int(input())
    print(f1(n) + f2(n))

