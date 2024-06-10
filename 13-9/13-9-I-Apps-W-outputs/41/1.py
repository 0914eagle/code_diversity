
def get_speedometer_error(d, s):
    # Calculate the true speed based on the distance and speedometer reading
    true_speed = d / s
    
    # Return the difference between the true speed and the speedometer reading
    return true_speed - s

def compute_constant_error(d_list, s_list):
    # Initialize the sum of the errors to zero
    total_error = 0
    
    # Iterate over the segments of the journey
    for i in range(len(d_list)):
        # Calculate the error for the current segment
        error = get_speedometer_error(d_list[i], s_list[i])
        
        # Add the error to the total error
        total_error += error
    
    # Return the average error
    return total_error / len(d_list)

def main():
    # Read the input data
    n, t = map(int, input().split())
    d_list = []
    s_list = []
    for i in range(n):
        d, s = map(int, input().split())
        d_list.append(d)
        s_list.append(s)
    
    # Compute the constant error
    constant_error = compute_constant_error(d_list, s_list)
    
    # Print the result
    print(constant_error)

if __name__ == '__main__':
    main()

