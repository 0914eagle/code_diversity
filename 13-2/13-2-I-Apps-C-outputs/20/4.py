
def balanced_equation(equation):
    # Split the equation into reactants and products
    reactants, products = equation.split("->")
    # Split the reactants and products into individual molecules
    reactant_molecules = reactants.split("+")
    product_molecules = products.split("+")
    # Create dictionaries to store the elements and their counts for the reactants and products
    reactant_elements = {}
    product_elements = {}
    for molecule in reactant_molecules:
        elements = molecule.split()
        for element in elements:
            if element not in reactant_elements:
                reactant_elements[element] = 1
            else:
                reactant_elements[element] += 1
    for molecule in product_molecules:
        elements = molecule.split()
        for element in elements:
            if element not in product_elements:
                product_elements[element] = 1
            else:
                product_elements[element] += 1
    # Find the least common multiple (LCM) of the counts for each element in the reactants and products
    lcm_dict = {}
    for element in reactant_elements:
        if element not in product_elements:
            lcm_dict[element] = reactant_elements[element]
        else:
            lcm_dict[element] = find_lcm(reactant_elements[element], product_elements[element])
    for element in product_elements:
        if element not in reactant_elements:
            lcm_dict[element] = product_elements[element]
        else:
            lcm_dict[element] = find_lcm(reactant_elements[element], product_elements[element])
    # Use the LCM to balance the equation
    balanced_equation = []
    for molecule in reactant_molecules:
        balanced_equation.append(balance_molecule(molecule, lcm_dict))
    balanced_equation.append("->")
    for molecule in product_molecules:
        balanced_equation.append(balance_molecule(molecule, lcm_dict))
    return " ".join(balanced_equation)

def balance_molecule(molecule, lcm_dict):
    elements = molecule.split()
    balanced_molecule = []
    for element in elements:
        count = lcm_dict[element]
        balanced_molecule.append(f"{element}{count}")
    return " ".join(balanced_molecule)

def find_lcm(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while True:
        if (a * b) % a == 0 and (a * b) % b == 0:
            return a * b
        a += 1

equation = "+1 2 H 2 O 1 +1 2 C 1 O 2 -1 1 O 2 -1 3 C 6 H 12 O 6 0 0"
print(balanced_equation(equation))

