
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def f(perm):
    gcds = []
    for i in range(len(perm)):
        gcds.append(gcd(perm[i], perm[i+1]))
    return len(set(gcds))

def f_max(n):
    max_f = 0
    for perm in itertools.permutations(range(1, n+1)):
        f_value = f(perm)
        if f_value > max_f:
            max_f = f_value
    return max_f

def count_permutations(n):
    count = 0
    for perm in itertools.permutations(range(1, n+1)):
        if f(perm) == f_max(n):
            count += 1
    return count % 1000000007

if __name__ == '__main__':
    n = int(input())
    print(count_permutations(n))

