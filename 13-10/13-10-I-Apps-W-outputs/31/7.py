
def get_molecule(valences):
    # Initialize a dictionary to store the number of bonds between each pair of atoms
    bonds = {}
    
    # Iterate over the valence numbers and create a list of pairs of atoms that can form bonds
    for i in range(len(valences)):
        for j in range(i+1, len(valences)):
            if valences[i] > 0 and valences[j] > 0:
                bonds[(i, j)] = 1
    
    # While there are still unpaired atoms, iterate over the list of pairs of atoms and find a pair that can form a bond
    while any(valences):
        for i in range(len(valences)):
            for j in range(i+1, len(valences)):
                if valences[i] > 0 and valences[j] > 0 and (i, j) in bonds:
                    valences[i] -= 1
                    valences[j] -= 1
                    bonds[(i, j)] += 1
                    break
    
    # If there are still unpaired atoms, the molecule is impossible
    if any(valences):
        return "Impossible"
    
    # Otherwise, return the number of bonds between each pair of atoms
    return [bonds[(i, j)] for i in range(len(valences)) for j in range(i+1, len(valences))]

def main():
    valences = list(map(int, input().split()))
    print(*get_molecule(valences))

if __name__ == '__main__':
    main()

