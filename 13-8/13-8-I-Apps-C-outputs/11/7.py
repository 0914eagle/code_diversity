
def get_shortest_time(W, v_h, N, x_list, y_list, S, s_list):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[(x_list[i], y_list[i])] = float('inf')

    # Initialize a dictionary to store the maximum horizontal speed at each gate
    max_speed = {}
    for i in range(N):
        max_speed[(x_list[i], y_list[i])] = v_h

    # Initialize a dictionary to store the speed of each pair of skis at each gate
    speed = {}
    for i in range(S):
        speed[s_list[i]] = {}
        for j in range(N):
            speed[s_list[i]][(x_list[j], y_list[j])] = float('inf')

    # Loop through each gate and calculate the minimum time required to pass through it
    for i in range(N):
        for j in range(S):
            if speed[s_list[j]][(x_list[i], y_list[i])] > min_time[(x_list[i], y_list[i])] + s_list[j]:
                speed[s_list[j]][(x_list[i], y_list[i])] = min_time[(x_list[i], y_list[i])] + s_list[j]
                max_speed[(x_list[i], y_list[i])] = min(max_speed[(x_list[i], y_list[i])], speed[s_list[j]][(x_list[i], y_list[i])])

    # Find the shortest time to pass through all the gates
    shortest_time = float('inf')
    for i in range(N):
        shortest_time = min(shortest_time, min_time[(x_list[i], y_list[i])] + speed[s_list[0]][(x_list[i], y_list[i])])

    # Return the shortest time or "IMPOSSIBLE" if it is not possible to pass through all the gates
    if shortest_time == float('inf'):
        return "IMPOSSIBLE"
    else:
        return shortest_time

def main():
    W, v_h, N = map(int, input().split())
    x_list = []
    y_list = []
    for i in range(N):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    S = int(input())
    s_list = []
    for i in range(S):
        s_list.append(int(input()))
    print(get_shortest_time(W, v_h, N, x_list, y_list, S, s_list))

if __name__ == '__main__':
    main()

