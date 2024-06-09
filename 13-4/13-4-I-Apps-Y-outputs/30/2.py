
def get_input_molecule():
    input_molecule = input()
    k = int(input())
    return input_molecule, k

def get_output_molecule():
    output_molecule = input()
    return output_molecule

def get_maximum_number_of_output_molecules(input_molecule, output_molecule):
    input_molecule_dict = {}
    for atom in input_molecule:
        if atom.isupper():
            if atom not in input_molecule_dict:
                input_molecule_dict[atom] = 1
            else:
                input_molecule_dict[atom] += 1
    
    output_molecule_dict = {}
    for atom in output_molecule:
        if atom.isupper():
            if atom not in output_molecule_dict:
                output_molecule_dict[atom] = 1
            else:
                output_molecule_dict[atom] += 1
    
    maximum_number_of_output_molecules = 0
    for atom in output_molecule_dict:
        if atom in input_molecule_dict and input_molecule_dict[atom] >= output_molecule_dict[atom]:
            maximum_number_of_output_molecules += output_molecule_dict[atom]
        else:
            return 0
    
    return maximum_number_of_output_molecules

def main():
    input_molecule, k = get_input_molecule()
    output_molecule = get_output_molecule()
    maximum_number_of_output_molecules = get_maximum_number_of_output_molecules(input_molecule, output_molecule)
    print(maximum_number_of_output_molecules)

if __name__ == '__main__':
    main()

