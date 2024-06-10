
def get_maximum_power(M, S, steps):
    # Initialize variables
    power = 1
    max_power = 0
    no_ops = 0
    
    # Iterate through the steps
    for i in range(M):
        # Check if the current step is a + step
        if steps[i] == "+":
            # Add 1 to the power
            power += 1
        # Check if the current step is an x step
        elif steps[i] == "x":
            # Multiply the power by 2
            power *= 2
        
        # Check if the power exceeds the maximum power
        if power > max_power:
            # Update the maximum power
            max_power = power
        
        # Check if the power exceeds the strength
        if power > S:
            # Update the number of no-ops
            no_ops += 1
    
    # Return the maximum power and the number of no-ops
    return max_power, no_ops

def get_optimal_steps(M, S, steps):
    # Initialize variables
    max_power = 0
    optimal_steps = []
    
    # Iterate through the steps
    for i in range(M):
        # Check if the current step is a + step
        if steps[i] == "+":
            # Add 1 to the power
            power += 1
        # Check if the current step is an x step
        elif steps[i] == "x":
            # Multiply the power by 2
            power *= 2
        
        # Check if the power exceeds the maximum power
        if power > max_power:
            # Update the maximum power
            max_power = power
            # Update the optimal steps
            optimal_steps = steps[:i+1]
        
        # Check if the power exceeds the strength
        if power > S:
            # Update the number of no-ops
            no_ops += 1
    
    # Return the optimal steps
    return optimal_steps

def main():
    # Read the input
    M, S = map(int, input().split())
    steps = input()
    
    # Get the maximum power and the number of no-ops
    max_power, no_ops = get_maximum_power(M, S, steps)
    
    # Get the optimal steps
    optimal_steps = get_optimal_steps(M, S, steps)
    
    # Print the output
    print("".join(optimal_steps))
    print(no_ops)

if __name__ == '__main__':
    main()

