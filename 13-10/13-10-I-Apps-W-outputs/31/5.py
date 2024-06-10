
def get_bond_counts(valence_numbers):
    # Sort the valence numbers in descending order
    valence_numbers.sort(reverse=True)
    
    # Initialize the bond counts
    bond_counts = [0, 0, 0]
    
    # Iterate through the valence numbers
    for i in range(len(valence_numbers)):
        # Get the current valence number
        valence_number = valence_numbers[i]
        
        # Check if the current valence number is odd
        if valence_number % 2 == 1:
            # If the current valence number is odd, set the corresponding bond count to 1
            bond_counts[i] = 1
            
            # Decrement the current valence number by 1
            valence_number -= 1
            
        # While the current valence number is even
        while valence_number > 0:
            # Increment the corresponding bond count
            bond_counts[i] += 1
            
            # Decrement the current valence number by 2
            valence_number -= 2
    
    # Return the bond counts
    return bond_counts

def main():
    # Read the valence numbers from stdin
    valence_numbers = list(map(int, input().split()))
    
    # Get the bond counts
    bond_counts = get_bond_counts(valence_numbers)
    
    # Print the bond counts
    print(*bond_counts)

if __name__ == '__main__':
    main()

