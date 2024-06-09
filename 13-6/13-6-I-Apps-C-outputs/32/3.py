
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    times = []
    for _ in range(N):
        times.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for row in times for t in row)
    return N, M, times

def f1(N, M, times):
    # Initialize the state of the system
    state = [0] * M
    for i in range(N):
        for j in range(M):
            state[j] = max(state[j], times[i][j])
    return sum(state)

def f2(N, M, times):
    # Initialize the state of the system
    state = [0] * M
    for i in range(N):
        for j in range(M):
            state[j] = max(state[j], times[i][j])
    
    # Sort the state in descending order
    state.sort(reverse=True)
    
    # Calculate the total waiting time
    total_time = 0
    for i in range(N):
        for j in range(M):
            total_time += state[j]
            state[j] -= 1
    
    return total_time

if __name__ == '__main__':
    N, M, times = get_input()
    print(f2(N, M, times))

