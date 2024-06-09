
def get_input_molecule():
    molecule = input()
    k = int(input())
    return molecule, k

def get_output_molecule():
    return input()

def get_max_number_of_output_molecules(input_molecule, input_molecule_count, output_molecule):
    # Your code here
    return 0

def main():
    input_molecule, input_molecule_count = get_input_molecule()
    output_molecule = get_output_molecule()
    max_number_of_output_molecules = get_max_number_of_output_molecules(input_molecule, input_molecule_count, output_molecule)
    print(max_number_of_output_molecules)

if __name__ == '__main__':
    main()

