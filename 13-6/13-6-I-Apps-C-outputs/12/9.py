
import math

def get_max_distance(N, T, s, a):
    max_distance = 0
    for i in range(N):
        distance = max(0, T[i] - s[i] * math.fabs(a[i] - math.pi/2))
        max_distance += distance
    return max_distance

def main():
    N = int(input())
    T = []
    s = []
    a = []
    for i in range(N):
        T.append(float(input()))
        s.append(float(input()))
        a.append(float(input()))
    print(get_max_distance(N, T, s, a))

if __name__ == '__main__':
    main()

