
def get_synchronization_sequence(grigory_charges, andrew_charges):
    # Initialize the sequence of synchronization operations
    sequence = []
    
    # Loop through the stones
    for i in range(len(grigory_charges)):
        # If the charges are not equal, add a synchronization operation to the sequence
        if grigory_charges[i] != andrew_charges[i]:
            sequence.append(i)
    
    # Return the sequence of synchronization operations
    return sequence

def perform_synchronization(grigory_charges, sequence):
    # Loop through the sequence of synchronization operations
    for i in sequence:
        # Synchronize the stone at index i with its neighbors
        grigory_charges[i] = grigory_charges[i + 1] + grigory_charges[i - 1] - grigory_charges[i]
    
    # Return the updated charges
    return grigory_charges

def main():
    # Read the input
    n = int(input())
    grigory_charges = list(map(int, input().split()))
    andrew_charges = list(map(int, input().split()))
    
    # Get the sequence of synchronization operations
    sequence = get_synchronization_sequence(grigory_charges, andrew_charges)
    
    # Perform the synchronization operations
    grigory_charges = perform_synchronization(grigory_charges, sequence)
    
    # Check if the charges are equal
    if grigory_charges == andrew_charges:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

