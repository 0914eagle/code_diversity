
import math

def cost(subset, k):
    return math.pow(len(subset), k)

def sum_of_costs(subsets, k):
    return sum([cost(subset, k) for subset in subsets]) % (10**9 + 7)

def non_empty_subsets(n):
    subsets = []
    for i in range(1, n+1):
        subsets.extend(combinations(range(1, n+1), i))
    return subsets

def main():
    n, k = map(int, input().split())
    subsets = non_empty_subsets(n)
    print(sum_of_costs(subsets, k))

if __name__ == '__main__':
    main()

