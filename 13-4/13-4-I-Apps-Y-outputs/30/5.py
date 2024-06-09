
def get_input_molecule():
    input_molecule = input()
    return input_molecule

def get_output_molecule():
    output_molecule = input()
    return output_molecule

def get_number_of_input_molecules():
    number_of_input_molecules = int(input())
    return number_of_input_molecules

def get_maximum_number_of_output_molecules(input_molecule, output_molecule, number_of_input_molecules):
    maximum_number_of_output_molecules = 0
    for i in range(number_of_input_molecules):
        if input_molecule == output_molecule:
            maximum_number_of_output_molecules += 1
        else:
            maximum_number_of_output_molecules += 0
    return maximum_number_of_output_molecules

def main():
    input_molecule = get_input_molecule()
    output_molecule = get_output_molecule()
    number_of_input_molecules = get_number_of_input_molecules()
    maximum_number_of_output_molecules = get_maximum_number_of_output_molecules(input_molecule, output_molecule, number_of_input_molecules)
    print(maximum_number_of_output_molecules)

if __name__ == '__main__':
    main()

