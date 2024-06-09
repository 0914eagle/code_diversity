
def get_input_molecule():
    molecule = input()
    k = int(input())
    return molecule, k

def get_output_molecule():
    return input()

def get_molecule_count(input_molecule, output_molecule):
    input_count = 0
    output_count = 0
    for atom in input_molecule:
        if atom == output_molecule[0]:
            output_count += 1
        else:
            input_count += 1
    return input_count, output_count

def get_maximum_output(input_count, output_count):
    return min(input_count, output_count)

def main():
    input_molecule, k = get_input_molecule()
    output_molecule = get_output_molecule()
    input_count, output_count = get_molecule_count(input_molecule, output_molecule)
    maximum_output = get_maximum_output(input_count, output_count)
    print(maximum_output)

if __name__ == '__main__':
    main()

