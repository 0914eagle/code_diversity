
def get_molecule_configuration(valence_numbers):
    # Sort the valence numbers in descending order
    valence_numbers.sort(reverse=True)
    
    # Initialize the molecule configuration as a dictionary with keys as atom indices and values as the number of bonds between that atom and the next atom in the cycle
    molecule_configuration = {i: 0 for i in range(1, len(valence_numbers) + 1)}
    
    # Set the first atom as the starting atom
    current_atom = 1
    
    # Iterate through the valence numbers and form bonds between atoms
    for valence_number in valence_numbers:
        # Find the next atom in the cycle
        next_atom = current_atom + 1
        if next_atom > len(valence_numbers):
            next_atom = 1
        
        # Form a bond between the current and next atom
        molecule_configuration[current_atom] += 1
        molecule_configuration[next_atom] += 1
        
        # Update the current atom
        current_atom = next_atom
    
    return molecule_configuration

def main():
    valence_numbers = list(map(int, input().split()))
    molecule_configuration = get_molecule_configuration(valence_numbers)
    
    # Check if the molecule configuration is possible
    if all(bond_count == valence_number for bond_count, valence_number in zip(molecule_configuration.values(), valence_numbers)):
        print(*molecule_configuration.values())
    else:
        print("Impossible")

if __name__ == '__main__':
    main()

