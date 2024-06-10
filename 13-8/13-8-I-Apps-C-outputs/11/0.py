
def get_fastest_ski_pair(W, v_h, N, y, x, S, s):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time_required = {}
    for i in range(N):
        min_time_required[i] = float('inf')
    
    # Initialize a dictionary to store the minimum speed required to pass through each gate
    min_speed_required = {}
    for i in range(N):
        min_speed_required[i] = float('inf')
    
    # Loop through each gate and calculate the minimum time and speed required to pass through it
    for i in range(N):
        for j in range(S):
            time_required = (y[i] - y[i-1]) / s[j] + (x[i] - x[i-1]) / v_h
            if time_required < min_time_required[i]:
                min_time_required[i] = time_required
                min_speed_required[i] = s[j]
    
    # Find the gate with the minimum time required to pass through it
    min_time_gate = 0
    for i in range(1, N):
        if min_time_required[i] < min_time_required[min_time_gate]:
            min_time_gate = i
    
    # Find the gate with the minimum speed required to pass through it
    min_speed_gate = 0
    for i in range(1, N):
        if min_speed_required[i] < min_speed_required[min_speed_gate]:
            min_speed_gate = i
    
    # If the minimum time gate is not the last gate, then it is impossible to pass through the race course
    if min_time_gate != N-1:
        return -1
    
    # Return the minimum speed required to pass through the last gate
    return min_speed_required[min_speed_gate]

def main():
    W, v_h, N = map(int, input().split())
    y = []
    x = []
    for i in range(N):
        y_i, x_i = map(int, input().split())
        y.append(y_i)
        x.append(x_i)
    S = int(input())
    s = []
    for i in range(S):
        s.append(int(input()))
    
    fastest_ski_pair = get_fastest_ski_pair(W, v_h, N, y, x, S, s)
    if fastest_ski_pair == -1:
        print("IMPOSSIBLE")
    else:
        print(fastest_ski_pair)

if __name__ == '__main__':
    main()

