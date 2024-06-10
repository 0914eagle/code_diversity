
import itertools

def get_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    return sorted(factors)

def solve(n, k, S):
    factors = [get_factors(i) for i in range(1, n + 1)]
    chosen_cubes = []
    sticker_positions = []
    for i in range(k):
        chosen_cubes.append(0)
        sticker_positions.append(0)
    
    def recurse(i, current_sum):
        if i == n:
            if current_sum == S:
                yield chosen_cubes[:]
        else:
            for j in range(len(factors[i])):
                chosen_cubes[i] = factors[i][j]
                for result in recurse(i + 1, current_sum + chosen_cubes[i]):
                    yield result
    
    count = 0
    for result in recurse(0, 0):
        count += 1
    
    return count

def main():
    n, k, S = map(int, input().split())
    print(solve(n, k, S))

if __name__ == '__main__':
    main()

