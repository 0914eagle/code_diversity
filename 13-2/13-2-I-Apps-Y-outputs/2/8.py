
def get_max_output(input_molecule, input_count, output_molecule):
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)
    max_output = 0
    for i in range(input_count):
        if can_construct(input_atoms, output_atoms):
            max_output += 1
    return max_output

def parse_molecule(molecule):
    atoms = {}
    for atom in molecule:
        if atom.isupper():
            atoms[atom] = atoms.get(atom, 0) + 1
        else:
            atoms[atom.upper()] = atoms.get(atom.upper(), 0) + int(atom)
    return atoms

def can_construct(input_atoms, output_atoms):
    for atom, count in output_atoms.items():
        if input_atoms.get(atom, 0) < count:
            return False
    return True

