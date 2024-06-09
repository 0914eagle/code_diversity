
import math

def number_of_permutations(n, k):
    return math.factorial(n) // math.factorial(n - k)

def main():
    n, k = map(int, input().split())
    print(number_of_permutations(n, k) % (2**31 - 1))

if __name__ == "__main__":
    main()

