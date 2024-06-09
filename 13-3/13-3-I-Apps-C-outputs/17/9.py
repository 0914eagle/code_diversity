
import sys

def f1(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    # in the n x m grid to prevent Alice from placing her 2 x 2 block
    count = 0
    for i in range(n):
        for j in range(m):
            if i + 1 < n and j + 1 < m:
                count += 1
    return count % p

def f2(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    # in the n x m grid to prevent Alice from placing her 2 x 2 block
    # and output the result modulo p
    count = f1(n, m, p)
    return count % p

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    print(f2(n, m, p))

