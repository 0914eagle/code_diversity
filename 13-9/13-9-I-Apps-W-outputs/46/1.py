
import sys

def euler_phi(n):
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result -= result // i
            while n % i == 0:
                n //= i
    if n > 1:
        result -= result // n
    return result

def generate_permutations(n):
    permutations = []
    for i in range(n):
        permutations.append(list(range(1, n + 1)))
    return permutations

def count_distinct_gcds(permutation):
    gcds = set()
    for i in range(len(permutation)):
        gcds.add(euler_phi(permutation[i]))
    return len(gcds)

def solve(n):
    permutations = generate_permutations(n)
    max_distinct_gcds = 0
    count = 0
    for permutation in permutations:
        distinct_gcds = count_distinct_gcds(permutation)
        if distinct_gcds > max_distinct_gcds:
            max_distinct_gcds = distinct_gcds
            count = 1
        elif distinct_gcds == max_distinct_gcds:
            count += 1
    return count

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(solve(n) % 1000000007)

