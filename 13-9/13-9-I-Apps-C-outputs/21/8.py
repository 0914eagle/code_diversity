
import math

def number_of_permutations(N, K):
    return math.factorial(N) // math.factorial(N - K)

def main():
    N, K = map(int, input().split())
    print(number_of_permutations(N, K))

if __name__ == "__main__":
    main()

