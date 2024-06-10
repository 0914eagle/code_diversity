
def get_max_power(steps, strength):
    # Initialize variables
    current_power = 1
    max_power = 1
    no_ops = []

    # Iterate through the steps
    for i, step in enumerate(steps):
        # If the step is a plus step, add 1 to the current power
        if step == "+":
            current_power += 1
        # If the step is an x step, multiply the current power by 2
        elif step == "x":
            current_power *= 2
        # If the current power exceeds the maximum power, update the maximum power
        if current_power > max_power:
            max_power = current_power
        # If the current power exceeds the strength, add the current step to the list of no-ops
        if current_power > strength:
            no_ops.append(i)
    
    # Return the list of no-ops
    return no_ops

def get_output_string(steps, no_ops):
    # Initialize the output string
    output = ""

    # Iterate through the steps
    for i, step in enumerate(steps):
        # If the step is a no-op, replace it with an o
        if i in no_ops:
            output += "o"
        # Otherwise, replace it with the original step
        else:
            output += step
    
    # Return the output string
    return output

if __name__ == '__main__':
    # Read the input
    m, s = map(int, input().split())
    steps = input()

    # Get the list of no-ops
    no_ops = get_max_power(steps, s)

    # Get the output string
    output = get_output_string(steps, no_ops)

    # Print the output
    print(output)

