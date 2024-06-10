
def get_max_power(m, s, steps):
    # Initialize variables
    power = 1
    max_power = 0
    no_op_steps = []
    
    # Iterate through the steps
    for i, step in enumerate(steps):
        # If the step is a + step, add 1 to the power
        if step == '+':
            power += 1
        # If the step is a x step, multiply the power by 2
        elif step == 'x':
            power *= 2
        # If the power is greater than the maximum power, update the maximum power
        if power > max_power:
            max_power = power
        # If the power is less than or equal to the strength, add the step to the list of no-op steps
        elif power <= s:
            no_op_steps.append(i)
    
    # Return the list of no-op steps
    return no_op_steps

def get_output_string(m, s, steps, no_op_steps):
    # Initialize the output string
    output = ''
    
    # Iterate through the steps
    for i, step in enumerate(steps):
        # If the step is a no-op step, replace it with an o
        if i in no_op_steps:
            output += 'o'
        # Otherwise, replace it with the original step
        else:
            output += step
    
    # Return the output string
    return output

def main():
    # Read the input
    m, s = map(int, input().split())
    steps = input()
    
    # Get the list of no-op steps
    no_op_steps = get_max_power(m, s, steps)
    
    # Get the output string
    output = get_output_string(m, s, steps, no_op_steps)
    
    # Print the output
    print(output)

if __name__ == '__main__':
    main()

