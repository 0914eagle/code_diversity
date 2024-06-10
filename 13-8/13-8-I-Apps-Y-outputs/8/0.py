
def find_optimal_umbrellas(a, n, m, rain_segments, umbrellas):
    # Initialize a list to store the optimal umbrellas
    optimal_umbrellas = []
    
    # Loop through each umbrella
    for i in range(m):
        # Get the current umbrella's location and weight
        x_i, p_i = umbrellas[i]
        
        # Check if the current umbrella's location is in the rain
        in_rain = False
        for segment in rain_segments:
            if segment[0] <= x_i <= segment[1]:
                in_rain = True
                break
        
        # If the current umbrella's location is in the rain, add it to the optimal umbrellas
        if in_rain:
            optimal_umbrellas.append(i)
    
    # Return the optimal umbrellas
    return optimal_umbrellas

def calculate_fatigue(a, n, m, rain_segments, umbrellas, optimal_umbrellas):
    # Initialize a variable to store the total fatigue
    total_fatigue = 0
    
    # Loop through each umbrella
    for i in range(m):
        # Get the current umbrella's location and weight
        x_i, p_i = umbrellas[i]
        
        # Check if the current umbrella's location is in the rain
        in_rain = False
        for segment in rain_segments:
            if segment[0] <= x_i <= segment[1]:
                in_rain = True
                break
        
        # If the current umbrella's location is in the rain and it is an optimal umbrella, add its weight to the total fatigue
        if in_rain and i in optimal_umbrellas:
            total_fatigue += p_i
    
    # Return the total fatigue
    return total_fatigue

def main():
    # Read the input
    a, n, m = map(int, input().split())
    rain_segments = []
    umbrellas = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        rain_segments.append([l_i, r_i])
    for i in range(m):
        x_i, p_i = map(int, input().split())
        umbrellas.append([x_i, p_i])
    
    # Find the optimal umbrellas
    optimal_umbrellas = find_optimal_umbrellas(a, n, m, rain_segments, umbrellas)
    
    # Calculate the total fatigue
    total_fatigue = calculate_fatigue(a, n, m, rain_segments, umbrellas, optimal_umbrellas)
    
    # Print the total fatigue
    print(total_fatigue)

if __name__ == '__main__':
    main()

