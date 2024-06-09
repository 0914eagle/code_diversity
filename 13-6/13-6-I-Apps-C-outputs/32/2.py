
def get_input():
    N, M = map(int, input().split())
    assert 2 <= N <= 50 and 2 <= M <= 50
    food_times = []
    for _ in range(N):
        food_times.append(list(map(int, input().split())))
    assert all(1 <= t <= 200 for row in food_times for t in row)
    return N, M, food_times

def solve(N, M, food_times):
    # Initialize a 2D array to store the minimum time to eat from each bowl
    min_time = [[float('inf') for _ in range(M)] for _ in range(N)]
    # Initialize a 2D array to store the previous bowl eaten from
    prev_bowl = [[-1 for _ in range(M)] for _ in range(N)]
    
    # Initialize the minimum time to eat from the first bowl
    min_time[0][0] = 0
    prev_bowl[0][0] = 0
    
    # Loop through each dog
    for i in range(N):
        # Loop through each bowl
        for j in range(M):
            # If the current bowl has not been eaten from before
            if min_time[i][j] == float('inf'):
                # Set the minimum time to eat from the current bowl to the maximum time of the previous bowl
                min_time[i][j] = max(min_time[i - 1][k] for k in range(M))
                # Set the previous bowl eaten from to the current bowl
                prev_bowl[i][j] = j
    
    # Return the minimum total waiting time
    return sum(min_time[N - 1][j] + food_times[N - 1][j] for j in range(M))

if __name__ == '__main__':
    N, M, food_times = get_input()
    print(solve(N, M, food_times))

