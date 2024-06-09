
def crafting_system(materials, recipes):
    # Initialize a dictionary to store the required materials
    required_materials = {}

    # Loop through each recipe
    for recipe in recipes:
        # Extract the input and output materials and the quantity of output materials
        input_material, output_material, quantity = recipe

        # Check if the output material is already in the required materials dictionary
        if output_material not in required_materials:
            # If not, add it to the dictionary with the required quantity
            required_materials[output_material] = quantity
        else:
            # If it is already in the dictionary, update the required quantity
            required_materials[output_material] += quantity

        # Check if the input material is already in the required materials dictionary
        if input_material not in required_materials:
            # If not, add it to the dictionary with the required quantity
            required_materials[input_material] = -quantity
        else:
            # If it is already in the dictionary, update the required quantity
            required_materials[input_material] -= quantity

    # Loop through each material and its required quantity
    for material, quantity in required_materials.items():
        # If the required quantity is positive, add it to the total required quantity
        if quantity > 0:
            materials[material] += quantity

    # Return the total required materials
    return materials

