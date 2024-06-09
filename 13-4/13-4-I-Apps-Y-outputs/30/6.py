
def f1(input_molecule, input_count, output_molecule):
    # Split the input molecule into a list of atoms
    input_atoms = input_molecule.split()
    # Split the output molecule into a list of atoms
    output_atoms = output_molecule.split()
    # Initialize a dictionary to store the count of each atom in the input molecule
    input_atom_count = {}
    for atom in input_atoms:
        if atom.isalpha():
            input_atom_count[atom] = input_atom_count.get(atom, 0) + 1
        else:
            input_atom_count[atom[:-1]] = input_atom_count.get(atom[:-1], 0) + int(atom[-1])
    
    # Initialize a dictionary to store the count of each atom in the output molecule
    output_atom_count = {}
    for atom in output_atoms:
        if atom.isalpha():
            output_atom_count[atom] = output_atom_count.get(atom, 0) + 1
        else:
            output_atom_count[atom[:-1]] = output_atom_count.get(atom[:-1], 0) + int(atom[-1])
    
    # Initialize the maximum number of output molecules to 0
    max_output_count = 0
    
    # Iterate through the input molecule and check if we have enough atoms to form the output molecule
    for atom in output_atom_count:
        if input_atom_count.get(atom, 0) < output_atom_count[atom]:
            return 0
        else:
            max_output_count += input_atom_count[atom] // output_atom_count[atom]
    
    return max_output_count * input_count

def f2(input_molecule, input_count, output_molecule):
    # Split the input molecule into a list of atoms
    input_atoms = input_molecule.split()
    # Split the output molecule into a list of atoms
    output_atoms = output_molecule.split()
    # Initialize a dictionary to store the count of each atom in the input molecule
    input_atom_count = {}
    for atom in input_atoms:
        if atom.isalpha():
            input_atom_count[atom] = input_atom_count.get(atom, 0) + 1
        else:
            input_atom_count[atom[:-1]] = input_atom_count.get(atom[:-1], 0) + int(atom[-1])
    
    # Initialize a dictionary to store the count of each atom in the output molecule
    output_atom_count = {}
    for atom in output_atoms:
        if atom.isalpha():
            output_atom_count[atom] = output_atom_count.get(atom, 0) + 1
        else:
            output_atom_count[atom[:-1]] = output_atom_count.get(atom[:-1], 0) + int(atom[-1])
    
    # Initialize the maximum number of output molecules to 0
    max_output_count = 0
    
    # Iterate through the input molecule and check if we have enough atoms to form the output molecule
    for atom in output_atom_count:
        if input_atom_count.get(atom, 0) < output_atom_count[atom]:
            return 0
        else:
            max_output_count += input_atom_count[atom] // output_atom_count[atom]
    
    return max_output_count * input_count

if __name__ == '__main__':
    input_molecule = input()
    input_count = int(input())
    output_molecule = input()
    print(f1(input_molecule, input_count, output_molecule))
    print(f2(input_molecule, input_count, output_molecule))

