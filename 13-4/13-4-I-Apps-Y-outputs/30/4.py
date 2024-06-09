
def get_input_molecule():
    input_molecule = input()
    return input_molecule

def get_output_molecule():
    output_molecule = input()
    return output_molecule

def get_number_of_input_molecules():
    number_of_input_molecules = int(input())
    return number_of_input_molecules

def get_input_molecule_atoms(input_molecule):
    atoms = {}
    for atom in input_molecule:
        if atom.isupper():
            if atom not in atoms:
                atoms[atom] = 1
            else:
                atoms[atom] += 1
    return atoms

def get_output_molecule_atoms(output_molecule):
    atoms = {}
    for atom in output_molecule:
        if atom.isupper():
            if atom not in atoms:
                atoms[atom] = 1
            else:
                atoms[atom] += 1
    return atoms

def can_construct_output_molecule(input_molecule_atoms, output_molecule_atoms):
    for atom, count in output_molecule_atoms.items():
        if atom not in input_molecule_atoms or input_molecule_atoms[atom] < count:
            return False
    return True

def get_maximum_number_of_output_molecules(input_molecule, output_molecule):
    input_molecule_atoms = get_input_molecule_atoms(input_molecule)
    output_molecule_atoms = get_output_molecule_atoms(output_molecule)
    number_of_input_molecules = get_number_of_input_molecules()
    maximum_number_of_output_molecules = 0
    for i in range(number_of_input_molecules):
        if can_construct_output_molecule(input_molecule_atoms, output_molecule_atoms):
            maximum_number_of_output_molecules += 1
            input_molecule_atoms = get_input_molecule_atoms(input_molecule)
            output_molecule_atoms = get_output_molecule_atoms(output_molecule)
    return maximum_number_of_output_molecules

if __name__ == '__main__':
    input_molecule = get_input_molecule()
    output_molecule = get_output_molecule()
    maximum_number_of_output_molecules = get_maximum_number_of_output_molecules(input_molecule, output_molecule)
    print(maximum_number_of_output_molecules)

