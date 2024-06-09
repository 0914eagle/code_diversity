
def get_input_molecule():
    input_molecule = input()
    k = int(input())
    return input_molecule, k

def get_output_molecule():
    output_molecule = input()
    return output_molecule

def can_produce_output_molecule(input_molecule, output_molecule):
    input_atom_counts = get_atom_counts(input_molecule)
    output_atom_counts = get_atom_counts(output_molecule)
    for atom, count in output_atom_counts.items():
        if atom not in input_atom_counts or input_atom_counts[atom] < count:
            return False
    return True

def get_atom_counts(molecule):
    atom_counts = {}
    for atom in molecule:
        if atom.isupper():
            if atom not in atom_counts:
                atom_counts[atom] = 0
            atom_counts[atom] += 1
        else:
            current_atom = atom_counts[atom.upper()]
            atom_counts[atom.upper()] = current_atom - 1
    return atom_counts

def get_max_output_molecules(input_molecule, output_molecule, k):
    input_atom_counts = get_atom_counts(input_molecule)
    output_atom_counts = get_atom_counts(output_molecule)
    max_output_molecules = 0
    for atom, count in output_atom_counts.items():
        if atom in input_atom_counts and input_atom_counts[atom] >= count:
            max_output_molecules += input_atom_counts[atom] // count
    return max_output_molecules * k

def main():
    input_molecule, k = get_input_molecule()
    output_molecule = get_output_molecule()
    if can_produce_output_molecule(input_molecule, output_molecule):
        print(get_max_output_molecules(input_molecule, output_molecule, k))
    else:
        print(0)

if __name__ == '__main__':
    main()

