
def max_power(power, strength):
    # Calculate the maximum power that can be discharged
    max_discharge_power = power // (2 ** strength)
    # Return the number of no-op steps needed to reach the maximum power
    return max_discharge_power

def transform_spell(spell, strength):
    # Initialize variables
    no_op_steps = 0
    power = 1
    transformed_spell = ""
    # Iterate through the spell
    for step in spell:
        # If the step is a no-op step, increment the number of no-op steps
        if step == "o":
            no_op_steps += 1
        # If the step is a + step, add 1 to the power
        elif step == "+":
            power += 1
        # If the step is a x step, multiply the power by 2
        elif step == "x":
            power *= 2
        # If the power reaches the maximum discharge power, break the loop
        if power == max_power(power, strength):
            break
    # Add the no-op steps to the transformed spell
    transformed_spell += "o" * no_op_steps
    # Add the remaining steps to the transformed spell
    transformed_spell += spell[no_op_steps:]
    return transformed_spell

def main():
    # Read the input
    m, s = map(int, input().split())
    spell = input()
    # Transform the spell
    transformed_spell = transform_spell(spell, s)
    # Print the transformed spell
    print(transformed_spell)

if __name__ == '__main__':
    main()

