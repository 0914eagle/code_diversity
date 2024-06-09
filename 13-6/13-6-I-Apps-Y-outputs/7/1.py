
import math

def get_probability(n):
    return 1 - math.factorial(n) / (math.factorial(n) * n)

def main():
    n = int(input())
    print(get_probability(n))

if __name__ == '__main__':
    main()

