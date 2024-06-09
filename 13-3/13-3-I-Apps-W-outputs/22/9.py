
def crafting_system(materials, recipes):
    # Initialize a dictionary to store the required materials
    required_materials = {}

    # Loop through each recipe
    for recipe in recipes:
        # Extract the input and output materials and the quantity of output materials
        input_material, output_material, quantity = recipe

        # Check if the output material is in the required materials dictionary
        if output_material in required_materials:
            # If it is, add the quantity to the existing value
            required_materials[output_material] += quantity
        else:
            # If it's not, set the quantity as the new value
            required_materials[output_material] = quantity

        # Check if the input material is in the required materials dictionary
        if input_material in required_materials:
            # If it is, subtract the quantity from the existing value
            required_materials[input_material] -= quantity
        else:
            # If it's not, set the negative quantity as the new value
            required_materials[input_material] = -quantity

    # Loop through each material and its required quantity
    for material, quantity in required_materials.items():
        # If the quantity is positive, add it to the total required materials
        if quantity > 0:
            materials[material] += quantity

    # Return the total required materials
    return materials

