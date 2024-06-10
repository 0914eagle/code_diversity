
def get_molecule(atoms):
    # Initialize a dictionary to store the number of bonds for each atom
    bond_count = {}
    for atom in atoms:
        bond_count[atom] = 0
    
    # Iterate through the atoms and count the number of bonds for each atom
    for i in range(len(atoms)):
        for j in range(i+1, len(atoms)):
            atom1 = atoms[i]
            atom2 = atoms[j]
            if atom1 != atom2:
                bond_count[atom1] += 1
                bond_count[atom2] += 1
    
    # Check if the number of bonds for each atom is equal to its valence number
    for atom in atoms:
        if bond_count[atom] != atom:
            return "Impossible"
    
    # If all atoms have the correct number of bonds, return the bond counts
    bond_pairs = []
    for i in range(len(atoms)):
        for j in range(i+1, len(atoms)):
            atom1 = atoms[i]
            atom2 = atoms[j]
            if atom1 != atom2:
                bond_pairs.append(str(bond_count[atom1]))
                bond_pairs.append(str(bond_count[atom2]))
    
    return " ".join(bond_pairs)

def main():
    atoms = [int(atom) for atom in input().split()]
    print(get_molecule(atoms))

if __name__ == '__main__':
    main()

