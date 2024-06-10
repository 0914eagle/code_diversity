
import math

def compute_t(n, p, s, v):
    c = compute_c(n, p, s, v)
    return s * (1 + 1 / c) / v

def compute_c(n, p, s, v):
    return p * math.log2(n) * math.sqrt(2) / (s * v)

def main():
    n, p, s, v = map(float, input().split())
    t = compute_t(n, p, s, v)
    c = compute_c(n, p, s, v)
    print(t, c)

if __name__ == '__main__':
    main()

