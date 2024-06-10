
def get_optimal_umbrella_strategy(a, n, m, l, r, x, p):
    # Initialize a dictionary to store the optimal strategy
    strategy = {}
    
    # Loop through each point on the line
    for i in range(a):
        # If the point is in the rain, calculate the minimum fatigue
        if i in l:
            # Find the minimum fatigue by trying all possible umbrellas
            min_fatigue = float('inf')
            for j in range(m):
                # If the umbrella is located at the current point, calculate the fatigue
                if x[j] == i:
                    fatigue = p[j]
                # If the umbrella is not located at the current point, calculate the fatigue as 0
                else:
                    fatigue = 0
                # Update the minimum fatigue if necessary
                if fatigue < min_fatigue:
                    min_fatigue = fatigue
            # Add the minimum fatigue to the strategy dictionary
            strategy[i] = min_fatigue
        # If the point is not in the rain, calculate the fatigue as 0
        else:
            strategy[i] = 0
    
    # Return the strategy dictionary
    return strategy

def get_total_fatigue(a, n, m, l, r, x, p):
    # Get the optimal umbrella strategy
    strategy = get_optimal_umbrella_strategy(a, n, m, l, r, x, p)
    
    # Initialize the total fatigue
    total_fatigue = 0
    
    # Loop through each point on the line
    for i in range(a):
        # Add the fatigue at the current point to the total fatigue
        total_fatigue += strategy[i]
    
    # Return the total fatigue
    return total_fatigue

def main():
    # Read the input
    a, n, m = map(int, input().split())
    l = set()
    r = set()
    x = []
    p = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.add(l_i)
        r.add(r_i)
    for i in range(m):
        x_i, p_i = map(int, input().split())
        x.append(x_i)
        p.append(p_i)
    
    # Check if Polycarp can make his way from point 0 to point a
    if a in l:
        print(-1)
    else:
        # Get the total fatigue
        total_fatigue = get_total_fatigue(a, n, m, l, r, x, p)
        # Print the total fatigue
        print(total_fatigue)

if __name__ == '__main__':
    main()

