
def get_ski_speed(W, v_h, N, x, y, S, s):
    # Initialize the minimum time required to pass through all the gates
    min_time = float('inf')
    # Initialize the ski speed that allows you to pass through all the gates in the minimum time
    min_ski_speed = -1

    # Loop through each pair of skis
    for i in range(S):
        # Calculate the time required to pass through each gate with the current pair of skis
        time = 0
        for j in range(N):
            # Calculate the horizontal distance between the current gate and the previous gate
            horizontal_distance = x[j] - x[j-1] if j > 0 else x[0]
            # Calculate the vertical distance between the current gate and the previous gate
            vertical_distance = y[j] - y[j-1]
            # Calculate the time required to pass through the current gate with the current pair of skis
            time += max(horizontal_distance / v_h, vertical_distance / s[i])
        # If the time required to pass through all the gates with the current pair of skis is less than the minimum time, update the minimum time and the ski speed
        if time < min_time:
            min_time = time
            min_ski_speed = s[i]

    # Return the ski speed that allows you to pass through all the gates in the minimum time
    return min_ski_speed

def main():
    # Read the input
    W, v_h, N = map(int, input().split())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    S = int(input())
    s = []
    for i in range(S):
        s.append(int(input()))

    # Calculate the ski speed that allows you to pass through all the gates in the minimum time
    ski_speed = get_ski_speed(W, v_h, N, x, y, S, s)

    # Print the ski speed
    print(ski_speed)

if __name__ == '__main__':
    main()

