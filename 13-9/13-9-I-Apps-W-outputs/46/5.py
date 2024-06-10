
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def f(p):
    gcds = []
    for i in range(len(p)):
        gcds.append(gcd(p[i], p[i+1]))
    return len(set(gcds))

def f_max(n):
    max_value = 0
    for p in permutations(range(1, n+1)):
        value = f(p)
        if value > max_value:
            max_value = value
    return max_value

def count_permutations(n):
    count = 0
    for p in permutations(range(1, n+1)):
        if f(p) == f_max(n):
            count += 1
    return count % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    print(count_permutations(n))

