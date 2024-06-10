
import math

def get_lcm(a, b):
    return a * b // math.gcd(a, b)

def get_max_lcm(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            lcm = get_lcm(i, j)
            if lcm <= n:
                return lcm
    return 0

def main():
    n = int(input())
    print(get_max_lcm(n))

if __name__ == '__main__':
    main()

