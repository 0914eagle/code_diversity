
def f1(n, m):
    # Calculate the number of distinct subsequences of a sequence of length n
    # with elements from 1 to m, including the empty subsequence
    if n == 0:
        return 1
    else:
        return (m * f1(n-1, m)) % 1000000007

def f2(n, m):
    # Calculate the sum of f(a) over all sequences of length n with elements from 1 to m
    return sum(f1(i, m) for i in range(n+1)) % 1000000007

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f2(n, m))

