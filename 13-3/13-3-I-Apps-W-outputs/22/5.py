
def crafting_system(materials, recipes):
    # Initialize a dictionary to store the required materials
    required_materials = {}

    # Loop through each recipe
    for recipe in recipes:
        # Extract the input and output materials and their quantities
        input_material, input_quantity, output_material, output_quantity = recipe

        # Check if the output material is in the required materials dictionary
        if output_material in required_materials:
            # If it is, add the input quantity to the existing value
            required_materials[output_material] += input_quantity
        else:
            # If it's not, set the input quantity as the new value
            required_materials[output_material] = input_quantity

    # Loop through each material that Yraglac wants
    for material, quantity in materials.items():
        # Check if the material is in the required materials dictionary
        if material in required_materials:
            # If it is, add the quantity to the existing value
            required_materials[material] += quantity
        else:
            # If it's not, set the quantity as the new value
            required_materials[material] = quantity

    # Return the required materials dictionary
    return required_materials

