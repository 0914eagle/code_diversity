
def get_bond_configuration(valence_numbers):
    # Convert the valence numbers to a list of tuples, with each tuple containing a pair of atoms and their bond configuration
    bond_configurations = [(1, 1), (1, 1), (1, 1)]
    
    # Loop through the list of tuples and check if the sum of the bond configurations is equal to the valence number of each atom
    for i in range(len(bond_configurations)):
        atom1, atom2 = bond_configurations[i]
        if atom1 + atom2 != valence_numbers[i]:
            return "Impossible"
    
    # If all the bond configurations are valid, return the bond configurations as a list of integers
    return [atom1, atom2, atom3]

def main():
    valence_numbers = list(map(int, input().split()))
    print(get_bond_configuration(valence_numbers))

if __name__ == '__main__':
    main()

