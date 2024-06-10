
def get_skis(W, v_h, N, x_list, y_list, S, s_list):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[i] = float('inf')
    
    # Initialize a dictionary to store the minimum time required to pass through each gate with each pair of skis
    min_time_skis = {}
    for i in range(N):
        min_time_skis[i] = float('inf')
    
    # Loop through each pair of skis
    for j in range(S):
        # Initialize the current time to 0
        current_time = 0
        
        # Loop through each gate
        for i in range(N):
            # Calculate the time required to pass through the gate with the current pair of skis
            time_required = (y_list[i] - x_list[i]) / s_list[j]
            
            # Check if the time required is less than the minimum time required to pass through the gate
            if time_required < min_time[i]:
                # Update the minimum time required to pass through the gate
                min_time[i] = time_required
                
                # Update the minimum time required to pass through the gate with the current pair of skis
                min_time_skis[i] = time_required
            
            # Check if the time required is less than the current time
            if time_required < current_time:
                # Update the current time
                current_time = time_required
        
        # Check if the current time is less than the minimum time required to pass through all gates
        if current_time < min(min_time.values()):
            # Return the speed of the current pair of skis
            return s_list[j]
    
    # If no pair of skis can pass through all gates, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

def main():
    # Read the input
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
    
    # Call the get_skis function and print the result
    result = get_skis(W, v_h, N, x_list, y_list, S, s_list)
    print(result)

if __name__ == '__main__':
    main()

