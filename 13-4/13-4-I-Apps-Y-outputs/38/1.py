
def f1(N, X, x):
    # find the minimum distance between X and any city
    min_dist = min(abs(X - xi) for xi in x)
    # find the maximum value of D that can cover the minimum distance
    return min_dist

def f2(N, X, x):
    # find the maximum value of D that can cover all the cities
    max_dist = max(abs(X - xi) for xi in x)
    # return the maximum value of D
    return max_dist

if __name__ == '__main__':
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    print(f2(N, X, x))

