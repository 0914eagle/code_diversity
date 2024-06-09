
def get_max_output(input_molecule, input_count, output_molecule):
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)

    max_output = 0
    for i in range(input_count + 1):
        current_input = input_atoms.copy()
        current_input.subtract(output_atoms)
        if current_input.is_valid():
            max_output = max(max_output, i)

    return max_output

def parse_molecule(molecule):
    atoms = {}
    for atom in molecule:
        if atom.isupper():
            atoms[atom] = atoms.get(atom, 0) + 1
        else:
            atoms[atom.upper()] = atoms.get(atom.upper(), 0) + int(atom)
    return atoms

class Atoms:
    def __init__(self, atoms):
        self.atoms = atoms

    def subtract(self, other):
        for atom, count in other.atoms.items():
            self.atoms[atom] -= count
            if self.atoms[atom] == 0:
                del self.atoms[atom]

    def is_valid(self):
        for atom, count in self.atoms.items():
            if count < 0:
                return False
        return True

    def __repr__(self):
        return str(self.atoms)

