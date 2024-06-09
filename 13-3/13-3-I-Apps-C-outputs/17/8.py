
import sys

def f1(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    # in the n x m grid to prevent Alice from placing her 2 x 2 block
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            # Check if the current subgrid contains at least one obstacle
            if (i + 1) * (j + 1) >= 4:
                count += 1
    return count % p

def f2(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    # in the n x m grid to prevent Alice from placing her 2 x 2 block
    # using a recursive approach
    if n == 1 and m == 1:
        return 1
    if n == 1 or m == 1:
        return 2
    return (f2(n - 1, m, p) + f2(n, m - 1, p)) % p

if __name__ == '__main__':
    n, m, p = map(int, sys.stdin.readline().split())
    print(f1(n, m, p))

