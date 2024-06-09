
def f1(input_molecule, input_count, output_molecule):
    # Convert the input molecule string to a dictionary of atom counts
    atom_counts = {}
    for atom in input_molecule:
        if atom.isupper():
            if atom not in atom_counts:
                atom_counts[atom] = 1
            else:
                atom_counts[atom] += 1
        else:
            atom_counts[atom.upper()] = int(atom)

    # Convert the output molecule string to a dictionary of atom counts
    output_atom_counts = {}
    for atom in output_molecule:
        if atom.isupper():
            if atom not in output_atom_counts:
                output_atom_counts[atom] = 1
            else:
                output_atom_counts[atom] += 1
        else:
            output_atom_counts[atom.upper()] = int(atom)

    # Check if the input molecule can be converted to the output molecule
    can_convert = True
    for atom, count in output_atom_counts.items():
        if atom not in atom_counts or atom_counts[atom] < count:
            can_convert = False
            break

    # If the input molecule can be converted to the output molecule, return the maximum number of output molecules that can be produced
    if can_convert:
        return input_count * output_count // gcd(input_count, output_count)
    else:
        return 0

def f2(input_molecule, input_count, output_molecule):
    # Convert the input molecule string to a list of atom counts
    atom_counts = []
    for atom in input_molecule:
        if atom.isupper():
            atom_counts.append(1)
        else:
            atom_counts.append(int(atom))

    # Convert the output molecule string to a list of atom counts
    output_atom_counts = []
    for atom in output_molecule:
        if atom.isupper():
            output_atom_counts.append(1)
        else:
            output_atom_counts.append(int(atom))

    # Check if the input molecule can be converted to the output molecule
    can_convert = True
    for count in output_atom_counts:
        if count not in atom_counts:
            can_convert = False
            break

    # If the input molecule can be converted to the output molecule, return the maximum number of output molecules that can be produced
    if can_convert:
        return input_count * output_count // gcd(input_count, output_count)
    else:
        return 0

if __name__ == '__main__':
    input_molecule, input_count, output_molecule = input().split()
    print(f1(input_molecule, int(input_count), output_molecule))
    print(f2(input_molecule, int(input_count), output_molecule))

