
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(p):
    gcds = []
    for i in range(len(p)):
        gcds.append(gcd(p[i], p[i+1]))
    return len(set(gcds))

def count_permutations(n):
    permutations = []
    for i in range(n):
        permutations.append(list(range(1, n+1)))
    max_f = 0
    count = 0
    for p in permutations:
        f_val = f(p)
        if f_val > max_f:
            max_f = f_val
            count = 1
        elif f_val == max_f:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(count_permutations(n) % 1000000007)

