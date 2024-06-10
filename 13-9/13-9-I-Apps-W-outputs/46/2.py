
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def f(p):
    gcds = []
    for i in range(len(p)):
        gcds.append(gcd(p[i], p[i+1]))
    return len(set(gcds))

def f_max(n):
    max_f = 0
    for p in permutations(range(1, n+1)):
        max_f = max(max_f, f(p))
    return max_f

def count_permutations(n):
    count = 0
    for p in permutations(range(1, n+1)):
        if f(p) == f_max(n):
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(count_permutations(n) % 1000000007)

