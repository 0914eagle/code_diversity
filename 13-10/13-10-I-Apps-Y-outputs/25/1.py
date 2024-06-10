
import math

def approximate_tsp(n, p):
    c = 1.5
    t = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 10 ** 9)
    return t, c

def distribute_keys(s, v, t):
    c = (s * (1 + 1 / c)) / v
    return c

if __name__ == '__main__':
    n, p, s, v = map(float, input().split())
    t, c = approximate_tsp(n, p)
    c = distribute_keys(s, v, t)
    print(t, c)

