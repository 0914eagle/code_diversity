
def f1(n, m):
    # function to find the number of distinct routes
    return n * (n - 1) * (n - 2) * ... * (n - m + 1)

def f2(n, m):
    # function to find the number of distinct routes using a recursive approach
    if m == 0:
        return 1
    else:
        return n * f2(n - 1, m - 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

