
def get_input_molecule():
    input_molecule = input()
    k = int(input())
    return input_molecule, k

def get_output_molecule():
    output_molecule = input()
    return output_molecule

def get_molecule_count(input_molecule, output_molecule):
    input_dict = {}
    output_dict = {}

    for atom in input_molecule:
        if atom.isupper():
            if atom not in input_dict:
                input_dict[atom] = 1
            else:
                input_dict[atom] += 1

    for atom in output_molecule:
        if atom.isupper():
            if atom not in output_dict:
                output_dict[atom] = 1
            else:
                output_dict[atom] += 1

    count = 0
    for atom in output_dict:
        if atom in input_dict and input_dict[atom] >= output_dict[atom]:
            count += output_dict[atom]
        else:
            return 0

    return count

def main():
    input_molecule, k = get_input_molecule()
    output_molecule = get_output_molecule()
    count = get_molecule_count(input_molecule, output_molecule)
    print(count)

if __name__ == '__main__':
    main()

