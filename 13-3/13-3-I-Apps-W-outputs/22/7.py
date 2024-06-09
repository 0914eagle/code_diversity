
def crafting_system(materials, recipes):
    # Initialize a dictionary to store the required materials
    required_materials = {}

    # Loop through each recipe
    for recipe in recipes:
        # Get the input and output materials
        input_material, output_material, quantity = recipe

        # Check if the output material is already in the required materials dictionary
        if output_material not in required_materials:
            # If not, add it with the required quantity
            required_materials[output_material] = quantity
        else:
            # If it is already there, add the required quantity to the existing value
            required_materials[output_material] += quantity

        # Check if the input material is already in the required materials dictionary
        if input_material not in required_materials:
            # If not, add it with the required quantity
            required_materials[input_material] = quantity
        else:
            # If it is already there, subtract the required quantity from the existing value
            required_materials[input_material] -= quantity

    # Return the required materials
    return required_materials

