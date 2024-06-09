
def get_golorp_diet(golorp_name):
    # Initialize variables
    jaws_shape = len(golorp_name)
    stomach_size = 9
    variables = [str(i) for i in range(10)]
    diet = []

    # Iterate through the jaws shape
    for i in range(jaws_shape):
        # Get the current jaw position
        jaw_position = golorp_name.index("_")

        # Get the variable that can be fed to the jaw
        variable = variables[jaw_position]

        # Add the variable to the diet
        diet.append(variable)

        # Remove the variable from the list of available variables
        variables.remove(variable)

        # Move the jaw to the next position
        golorp_name = golorp_name[:jaw_position] + "_" + golorp_name[jaw_position+1:]

    # If the diet is not possible, return "false"
    if len(diet) > stomach_size:
        return "false"

    # Return the lexicographically smallest diet
    return "".join(diet)

