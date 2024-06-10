
def permutations(n):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    def f(p):
        gcds = []
        for i in range(n):
            gcds.append(gcd(p[i], p[(i+1)%n]))
        return len(set(gcds))
    
    def f_max(n):
        max_f = 0
        for p in permutations(n):
            f_val = f(p)
            if f_val > max_f:
                max_f = f_val
        return max_f
    
    def count_permutations(n):
        count = 0
        for p in permutations(n):
            if f(p) == f_max(n):
                count += 1
        return count
    
    return count_permutations(n)

if __name__ == '__main__':
    n = int(input())
    print(permutations(n) % 1000000007)

