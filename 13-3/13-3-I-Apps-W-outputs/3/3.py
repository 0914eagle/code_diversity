
def f1(n, x, edges):
    # Your code here
    return sum

def f2(...):
    # Your code here
    return sum

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(f1(n, x, edges) % (10**9 + 7))

