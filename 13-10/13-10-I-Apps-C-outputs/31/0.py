
def get_optimal_spell(spell, strength):
    # Initialize variables
    power = 1
    no_ops = 0
    optimal_spell = ""

    # Iterate through the spell
    for step in spell:
        # Check if the step is a + step
        if step == "+":
            # Increase the power by 1
            power += 1
        # Check if the step is a x step
        elif step == "x":
            # Double the power
            power *= 2
        # Check if the step is a no-op
        else:
            # Increase the number of no-ops
            no_ops += 1

        # Check if the power is less than or equal to the strength
        if power <= strength:
            # Add the step to the optimal spell
            optimal_spell += step
        # Check if the power is greater than the strength
        else:
            # Add a no-op to the optimal spell
            optimal_spell += "o"
            # Decrease the power by the strength
            power -= strength

    # Return the optimal spell
    return optimal_spell

def get_maximum_power(spell, strength):
    # Get the optimal spell
    optimal_spell = get_optimal_spell(spell, strength)

    # Initialize variables
    power = 1
    no_ops = 0

    # Iterate through the optimal spell
    for step in optimal_spell:
        # Check if the step is a + step
        if step == "+":
            # Increase the power by 1
            power += 1
        # Check if the step is a x step
        elif step == "x":
            # Double the power
            power *= 2
        # Check if the step is a no-op
        else:
            # Increase the number of no-ops
            no_ops += 1

    # Return the maximum power
    return power

if __name__ == '__main__':
    # Get the number of steps and the strength from the user
    m, s = map(int, input().split())
    spell = input()

    # Get the optimal spell and the maximum power
    optimal_spell = get_optimal_spell(spell, s)
    maximum_power = get_maximum_power(optimal_spell, s)

    # Print the optimal spell
    print(optimal_spell)

    # Print the maximum power
    print(maximum_power)

