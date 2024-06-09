
def get_materials_needed(materials_wanted, crafting_recipes):
    materials_needed = {}
    for material, amount in materials_wanted.items():
        materials_needed[material] = amount

    for recipe in crafting_recipes:
        input_material, output_material, amount = recipe
        if output_material not in materials_needed:
            materials_needed[output_material] = 0
        materials_needed[output_material] += amount * materials_needed[input_material]

    return [materials_needed[material] for material in sorted(materials_needed)]

