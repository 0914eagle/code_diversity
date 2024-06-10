
def count_symmetric_transitive_relations(n):
    count = 0
    for i in range(1, n+1):
        count += nCr(n, i) * (n-i) ** (n-1)
    return count % 1000000007

def nCr(n, r):
    if r == 0:
        return 1
    return n * nCr(n-1, r-1) // r

if __name__ == '__main__':
    n = int(input())
    print(count_symmetric_transitive_relations(n))

