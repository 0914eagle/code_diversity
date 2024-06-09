
def f1(n, m):
    # Calculate the number of subsequences for each sequence
    # and return the sum modulo 10^9 + 7
    return sum(f2(n, m, i) for i in range(1, m + 1)) % 1000000007

def f2(n, m, x):
    # Base case: if n is 1, return 1 if x is in the sequence, 0 otherwise
    if n == 1:
        return 1 if x in range(1, m + 1) else 0
    
    # Recursive case: calculate the number of subsequences for the first n - 1 elements
    # and return the sum modulo 10^9 + 7
    return sum(f2(n - 1, m, i) for i in range(1, x)) % 1000000007 + sum(f2(n - 1, m, i) for i in range(x + 1, m + 1)) % 1000000007

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

