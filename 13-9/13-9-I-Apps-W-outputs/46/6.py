
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(p):
    gcds = []
    for i in range(len(p)):
        gcds.append(gcd(p[i], p[i+1]))
    return len(set(gcds))

def f_max(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return max(f(p) for p in permutations)

def count_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutations.append(i)
    return len([p for p in permutations if f(p) == f_max(n)])

if __name__ == '__main__':
    n = int(input())
    print(count_permutations(n) % 1000000007)

