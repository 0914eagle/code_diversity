
import sys

def input_list():
    return list(map(int, sys.stdin.read().split()))

def solve(n, a, b):
    count = 0
    for i in range(1, n+1):
        if i != a and i != b:
            count += 1
    return count

def main():
    n, a, b = input_list()
    print(solve(n, a, b))

if __name__ == '__main__':
    main()

