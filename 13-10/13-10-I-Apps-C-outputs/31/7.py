
def get_steps(M, S):
    # Initialize the string of steps
    steps = "+" * M
    
    # Initialize the maximum power that can be discharged
    max_power = 1
    
    # Iterate through each step
    for i in range(M):
        # If the step is a + step, add 1 to the maximum power
        if steps[i] == "+":
            max_power += 1
        # If the step is an x step, multiply the maximum power by 2
        else:
            max_power *= 2
        
        # If the maximum power exceeds the strength, break the loop
        if max_power > S:
            break
    
    # Return the string of steps with the maximum power
    return steps[:i+1]

def main():
    # Read the input
    M, S = map(int, input().split())
    steps = input()
    
    # Get the string of steps with the maximum power
    max_steps = get_steps(M, S)
    
    # Print the output
    print(max_steps.replace("+", "o").replace("x", "o"))

if __name__ == '__main__':
    main()

