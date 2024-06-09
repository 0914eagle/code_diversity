
def get_input_molecule():
    input_molecule = input()
    return input_molecule

def get_output_molecule():
    output_molecule = input()
    return output_molecule

def get_input_quantity():
    input_quantity = int(input())
    return input_quantity

def get_output_quantity():
    output_quantity = int(input())
    return output_quantity

def get_input_molecule_dict(input_molecule):
    input_molecule_dict = {}
    for atom in input_molecule:
        if atom.isupper():
            if atom not in input_molecule_dict:
                input_molecule_dict[atom] = 1
            else:
                input_molecule_dict[atom] += 1
    return input_molecule_dict

def get_output_molecule_dict(output_molecule):
    output_molecule_dict = {}
    for atom in output_molecule:
        if atom.isupper():
            if atom not in output_molecule_dict:
                output_molecule_dict[atom] = 1
            else:
                output_molecule_dict[atom] += 1
    return output_molecule_dict

def can_construct_output_molecule(input_molecule_dict, output_molecule_dict):
    for atom, count in output_molecule_dict.items():
        if atom not in input_molecule_dict or input_molecule_dict[atom] < count:
            return False
    return True

def get_maximum_output_quantity(input_molecule_dict, output_molecule_dict):
    maximum_output_quantity = 0
    for atom, count in output_molecule_dict.items():
        maximum_output_quantity += input_molecule_dict[atom] // count
    return maximum_output_quantity

def main():
    input_molecule = get_input_molecule()
    output_molecule = get_output_molecule()
    input_quantity = get_input_quantity()
    output_quantity = get_output_quantity()
    input_molecule_dict = get_input_molecule_dict(input_molecule)
    output_molecule_dict = get_output_molecule_dict(output_molecule)
    if can_construct_output_molecule(input_molecule_dict, output_molecule_dict):
        maximum_output_quantity = get_maximum_output_quantity(input_molecule_dict, output_molecule_dict)
        print(maximum_output_quantity)
    else:
        print(0)

if __name__ == '__main__':
    main()

