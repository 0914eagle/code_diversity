
import math

def get_odd_probability(n):
    return int(n % 2 == 1)

def get_probability(n):
    return get_odd_probability(n) / n

if __name__ == '__main__':
    n = int(input())
    print(get_probability(n))

