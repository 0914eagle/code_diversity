
import math

def get_probability(N):
    return float(sum(1 for i in range(1, N+1, 2))) / N

def main():
    N = int(input())
    print(get_probability(N))

if __name__ == '__main__':
    main()

