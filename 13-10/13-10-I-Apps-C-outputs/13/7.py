
def permutations(n):
    if n == 1:
        return 1
    else:
        return n * permutations(n-1)

def combinations(n, k):
    return permutations(n) // permutations(k) // permutations(n-k)

def get_average_visitors(n, a, p):
    total = 0
    for i in range(combinations(n, i)):
        sum_a = sum(a[i])
        if sum_a <= p:
            total += 1
    return total / combinations(n, i)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = int(input())
    print(get_average_visitors(n, a, p))

