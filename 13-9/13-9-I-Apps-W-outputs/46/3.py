
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def f(p):
    gcds = []
    for i in range(len(p)):
        gcds.append(gcd(p[:i+1]))
    return len(set(gcds))

def f_max(n):
    permutations = []
    for i in range(n):
        permutations.append(list(range(1, n+1)))
    return max(f(p) for p in permutations)

def count_permutations(n):
    count = 0
    for i in range(n):
        for j in range(n):
            if f(list(range(1, n+1))) == f_max(n):
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(count_permutations(n) % 1000000007)

