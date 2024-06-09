
def f1(N, K, circle):
    # f1(N, K, circle) returns the number of distinct starting circles that give the same circle after K transformations as Stanko's original circle does after K transformations.
    return len(set(circle))

def f2(N, K, circle):
    # f2(N, K, circle) returns the number of distinct starting circles that give the same circle after K transformations as Stanko's original circle does after K transformations.
    return len(set(circle))

if __name__ == '__main__':
    N, K = map(int, input().split())
    circle = input()
    print(f1(N, K, circle))

