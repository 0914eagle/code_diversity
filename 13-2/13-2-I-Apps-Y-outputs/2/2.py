
def get_max_output(input_molecule, input_quantity, output_molecule):
    input_atoms = {}
    for atom in input_molecule:
        if atom.isupper():
            if atom not in input_atoms:
                input_atoms[atom] = 1
            else:
                input_atoms[atom] += 1
        else:
            input_atoms[atom.upper()] = int(atom.lower())

    output_atoms = {}
    for atom in output_molecule:
        if atom.isupper():
            if atom not in output_atoms:
                output_atoms[atom] = 1
            else:
                output_atoms[atom] += 1
        else:
            output_atoms[atom.upper()] = int(atom.lower())

    max_output = 0
    for atom, count in output_atoms.items():
        if atom in input_atoms and input_atoms[atom] >= count:
            max_output += count
        else:
            return 0

    return max_output // input_quantity

