
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def f(p):
    prefix = p[:len(p)]
    gcds = [gcd(prefix[i-1], prefix[i]) for i in range(1, len(prefix))]
    return len(set(gcds))

def f_max(n):
    permutations = list(itertools.permutations(range(1, n+1)))
    return max(f(p) for p in permutations)

def count_permutations(n):
    permutations = list(itertools.permutations(range(1, n+1)))
    return len([p for p in permutations if f(p) == f_max(n)])

def main():
    n = int(input())
    print((count_permutations(n) % 1000000007))

if __name__ == '__main__':
    main()

