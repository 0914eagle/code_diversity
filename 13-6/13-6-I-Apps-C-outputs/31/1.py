
def f1(n):
    # Calculate the number of ways to choose the values of s_i
    num_ways = 1
    for i in range(1, n+1):
        num_ways = (num_ways * i) % (10**9 + 7)
    return num_ways

def f2(n, t):
    # Calculate the number of ways to choose the values of s_i given the current state of the performers
    num_ways = 1
    for i in range(1, n+1):
        num_ways = (num_ways * (t[i-1]-i+1)) % (10**9 + 7)
    return num_ways

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f2(n, t))

