
def get_material_counts(material_counts, crafting_recipes):
    # Initialize a dictionary to store the counts of each material
    material_needed = {}

    # Loop through each material and its count
    for material, count in material_counts.items():
        # If the material is not already in the dictionary, add it with its count
        if material not in material_needed:
            material_needed[material] = count
        # If the material is already in the dictionary, add its count to the existing count
        else:
            material_needed[material] += count

    # Loop through each crafting recipe
    for recipe in crafting_recipes:
        # Get the input and output materials and counts
        input_material, input_count, output_material = recipe
        output_count = material_needed[output_material]

        # If the output material is not already in the dictionary, add it with its count
        if output_material not in material_needed:
            material_needed[output_material] = output_count
        # If the output material is already in the dictionary, add its count to the existing count
        else:
            material_needed[output_material] += output_count

        # Update the count of the input material
        material_needed[input_material] -= input_count * output_count

    return material_needed

