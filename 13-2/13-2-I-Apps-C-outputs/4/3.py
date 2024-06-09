
def f(n, k):
    if n == 0:
        return '.'
    else:
        return f(n-1, k-1)

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        print(f(n, k), end='')

