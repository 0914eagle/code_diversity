
def solve(a, n, m, segments, umbrellas):
    # Initialize the minimum fatigue and the optimal umbrella pickup and drop points
    min_fatigue = 0
    opt_pickup_points = []
    opt_drop_points = []
    
    # Loop through each umbrella and calculate the fatigue for each umbrella pickup and drop point
    for i in range(m):
        x_i, p_i = umbrellas[i]
        
        # Loop through each segment and calculate the fatigue for each segment pickup and drop point
        for j in range(n):
            l_j, r_j = segments[j]
            
            # Calculate the fatigue for picking up the umbrella at point x_i and dropping it at point l_j
            pickup_fatigue = p_i * (l_j - x_i)
            drop_fatigue = p_i * (r_j - l_j)
            total_fatigue = pickup_fatigue + drop_fatigue
            
            # If the total fatigue is less than the current minimum fatigue, update the minimum fatigue and the optimal pickup and drop points
            if total_fatigue < min_fatigue:
                min_fatigue = total_fatigue
                opt_pickup_points = [x_i]
                opt_drop_points = [l_j]
    
    # If the minimum fatigue is greater than the total distance between the starting point and the end point, return -1
    if min_fatigue > a:
        return -1
    
    # Otherwise, return the minimum fatigue and the optimal pickup and drop points
    return min_fatigue, opt_pickup_points, opt_drop_points

def main():
    a, n, m = map(int, input().split())
    segments = []
    umbrellas = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        segments.append((l_i, r_i))
    for i in range(m):
        x_i, p_i = map(int, input().split())
        umbrellas.append((x_i, p_i))
    min_fatigue, opt_pickup_points, opt_drop_points = solve(a, n, m, segments, umbrellas)
    print(min_fatigue)
    print(opt_pickup_points)
    print(opt_drop_points)

if __name__ == '__main__':
    main()

