
import math

def get_input():
    return int(input())

def is_odd(n):
    return n % 2 != 0

def solve(n):
    count = 0
    for i in range(1, n+1):
        if is_odd(i):
            count += 1
    return count / n

if __name__ == '__main__':
    n = get_input()
    print(solve(n))

