
import math

def get_ski_speed(W, v_h, N, x, y):
    # Calculate the minimum horizontal speed needed to pass through each gate
    min_h_speed = [math.ceil(W / (y[i+1] - y[i])) for i in range(N-1)]
    
    # Calculate the maximum vertical speed needed to pass through each gate
    max_v_speed = [math.ceil((x[i+1] - x[i]) / (y[i+1] - y[i])) for i in range(N-1)]
    
    # Calculate the minimum speed needed to pass through each gate
    min_speed = [max(min_h_speed[i], max_v_speed[i]) for i in range(N-1)]
    
    # Calculate the maximum speed needed to pass through each gate
    max_speed = [min(min_h_speed[i] + v_h, max_v_speed[i]) for i in range(N-1)]
    
    # Return the minimum speed needed to pass through all the gates
    return min(min_speed)

def get_fastest_ski_speed(W, v_h, N, x, y, S, s):
    # Initialize the fastest ski speed as 0
    fastest_ski_speed = 0
    
    # Iterate through all the possible ski speeds
    for i in range(S):
        # Calculate the ski speed for the current pair of skis
        ski_speed = get_ski_speed(W, v_h, N, x, y)
        
        # If the current pair of skis is faster than the previous fastest pair of skis, update the fastest ski speed
        if ski_speed > fastest_ski_speed:
            fastest_ski_speed = ski_speed
    
    # Return the fastest ski speed
    return fastest_ski_speed

def main():
    # Read the input
    W, v_h, N = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    S = int(input())
    s = list(map(int, input().split()))
    
    # Calculate the fastest ski speed
    fastest_ski_speed = get_fastest_ski_speed(W, v_h, N, x, y, S, s)
    
    # Print the fastest ski speed
    print(fastest_ski_speed)

if __name__ == '__main__':
    main()

