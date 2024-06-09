
def f1(n, m):
    return m == n

def f2(n, m):
    return "Yes" if m == n else "No"

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f2(n, m))

