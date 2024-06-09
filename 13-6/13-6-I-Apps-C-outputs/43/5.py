
import math

def f1(N, H, v, p):
    # Calculate the expected value for each hole
    ev = [0] * H
    for i in range(H):
        ev[i] = v[i] + p[i] * f1(N, H, v, p)
    return sum(ev)

def f2(N, H, v, p):
    # Calculate the expected value for each hole
    ev = [0] * H
    for i in range(H):
        ev[i] = v[i] + p[i] * f2(N, H, v, p)
    return sum(ev)

def main():
    N, H = map(int, input().split())
    v = list(map(int, input().split()))
    p = []
    for i in range(H):
        p.append(list(map(float, input().split())))
    print(round(f1(N, H, v, p), 4))

if __name__ == '__main__':
    main()

