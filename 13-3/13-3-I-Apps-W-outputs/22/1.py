
def crafting_system(materials, recipes):
    # Initialize a dictionary to store the required materials
    required_materials = {}

    # Loop through each recipe
    for recipe in recipes:
        # Get the input and output materials
        input_material, output_material, quantity = recipe

        # Check if the output material is in the required materials dictionary
        if output_material not in required_materials:
            # If not, set the required quantity to zero
            required_materials[output_material] = 0

        # Increment the required quantity by the recipe quantity
        required_materials[output_material] += quantity

    # Loop through each material in the required materials dictionary
    for material, quantity in required_materials.items():
        # Check if the material is in the materials list
        if material in materials:
            # If it is, subtract the required quantity from the available quantity
            materials[material] -= quantity

    # Return the updated materials list
    return materials

