
def find_molecule(valence_numbers):
    # Convert the valence numbers to a list of unique values
    unique_valence_numbers = list(set(valence_numbers))

    # Sort the list of unique valence numbers in descending order
    unique_valence_numbers.sort(reverse=True)

    # Initialize the number of bonds between each pair of atoms
    bonds = [0] * 3

    # Set the first bond between the 1st and 2nd atoms
    bonds[0] = 1

    # Set the first bond between the 2nd and 3rd atoms
    bonds[1] = 1

    # Set the first bond between the 3rd and 1st atoms
    bonds[2] = 1

    # Loop through each unique valence number
    for valence_number in unique_valence_numbers:
        # Find the index of the current valence number in the list of valence numbers
        index = valence_numbers.index(valence_number)

        # Check if the current valence number is greater than the number of bonds between the current and next atom
        if valence_number > bonds[index]:
            # Set the number of bonds between the current and next atom to the current valence number
            bonds[index] = valence_number

            # Set the number of bonds between the next and previous atom to the current valence number
            bonds[(index + 1) % 3] = valence_number

    # Check if the sum of the bonds is equal to the sum of the valence numbers
    if sum(bonds) == sum(valence_numbers):
        return bonds
    else:
        return "Impossible"

def main():
    valence_numbers = list(map(int, input().split()))
    print(*find_molecule(valence_numbers), sep=" ")

if __name__ == '__main__':
    main()

