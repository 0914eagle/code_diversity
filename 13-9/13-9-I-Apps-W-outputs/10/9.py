
import math

def get_min_time(a, b, n, taxis):
    min_time = math.inf
    for taxi in taxis:
        time = math.sqrt((taxi[0] - a) ** 2 + (taxi[1] - b) ** 2) / taxi[2]
        min_time = min(min_time, time)
    return min_time

def main():
    a, b = map(int, input().split())
    n = int(input())
    taxis = []
    for _ in range(n):
        x, y, v = map(int, input().split())
        taxis.append([x, y, v])
    print(get_min_time(a, b, n, taxis))

if __name__ == '__main__':
    main()

