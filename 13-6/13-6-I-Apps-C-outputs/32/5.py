
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    times = []
    for i in range(N):
        times.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for t in times)
    return N, M, times

def f1(N, M, times):
    # f1(N, M, times) should return the minimum total waiting time in seconds.
    # Your code here
    pass

def f2(N, M, times):
    # f2(N, M, times) should return the minimum total waiting time in seconds.
    # Your code here
    pass

if __name__ == '__main__':
    N, M, times = get_input()
    print(f1(N, M, times))
    print(f2(N, M, times))

