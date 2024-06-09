
def f1(n, q, x, y):
    # Your code here
    return x

def f2(n, q, x, y):
    # Your code here
    return y

if __name__ == '__main__':
    n = int(input())
    q = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(n, q, x, y))
    print(f2(n, q, x, y))

