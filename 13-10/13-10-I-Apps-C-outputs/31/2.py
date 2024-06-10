
def compute_max_power(steps, strength):
    # Initialize the maximum power to discharge
    max_power = 1
    # Initialize the number of + steps to 0
    num_plus_steps = 0
    # Initialize the number of x steps to 0
    num_x_steps = 0
    # Iterate through the steps
    for step in steps:
        # If the step is a + step, increase the number of + steps
        if step == "+":
            num_plus_steps += 1
        # If the step is an x step, increase the number of x steps
        elif step == "x":
            num_x_steps += 1
    # Calculate the maximum power to discharge
    max_power += num_plus_steps * 2 ** strength
    max_power += num_x_steps * (2 ** strength) ** 2
    return max_power

def convert_steps_to_no_ops(steps, strength):
    # Initialize the number of + steps to 0
    num_plus_steps = 0
    # Initialize the number of x steps to 0
    num_x_steps = 0
    # Initialize the number of no-op steps to 0
    num_no_op_steps = 0
    # Initialize the maximum power to discharge
    max_power = 1
    # Initialize the converted steps
    converted_steps = []
    # Iterate through the steps
    for step in steps:
        # If the step is a + step, increase the number of + steps
        if step == "+":
            num_plus_steps += 1
        # If the step is an x step, increase the number of x steps
        elif step == "x":
            num_x_steps += 1
        # If the step is a no-op step, increase the number of no-op steps
        else:
            num_no_op_steps += 1
    # Calculate the maximum power to discharge
    max_power += num_plus_steps * 2 ** strength
    max_power += num_x_steps * (2 ** strength) ** 2
    # Calculate the number of no-op steps to add
    num_no_op_steps_to_add = num_plus_steps + num_x_steps - int(max_power / (2 ** strength))
    # Add the no-op steps to the converted steps
    for i in range(num_no_op_steps_to_add):
        converted_steps.append("o")
    # Add the remaining steps to the converted steps
    for step in steps:
        if step not in converted_steps:
            converted_steps.append(step)
    return "".join(converted_steps)

def main():
    # Read the input
    num_steps, strength = map(int, input().split())
    steps = input()
    # Compute the maximum power to discharge
    max_power = compute_max_power(steps, strength)
    # Convert the steps to no-ops
    converted_steps = convert_steps_to_no_ops(steps, strength)
    # Print the converted steps
    print(converted_steps)

if __name__ == '__main__':
    main()

