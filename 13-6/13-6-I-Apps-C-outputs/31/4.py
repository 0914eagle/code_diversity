
import itertools

def f1(n):
    return n

def f2(n, t):
    # calculate the number of ways to choose s_i
    num_ways = 1
    for i in range(n):
        num_ways *= len(list(itertools.combinations(range(1, n+1), n-i)))
    return num_ways % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f2(n, t))

