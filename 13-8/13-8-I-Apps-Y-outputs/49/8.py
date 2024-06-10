
import math

def compute_time(n, p, s, v):
    c = 0
    time_taken = 0
    while True:
        time_taken = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 10 ** 9)
        if time_taken <= s / v:
            break
        c += 0.001
    return time_taken, c

def main():
    n, p, s, v = map(float, input().split())
    time_taken, c = compute_time(n, p, s, v)
    print(time_taken, c)

if __name__ == '__main__':
    main()

