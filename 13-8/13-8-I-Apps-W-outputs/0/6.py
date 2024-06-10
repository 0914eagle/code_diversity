
def get_synchronized_stones(charges, target_charges):
    # Initialize the synchronized stones as the original charges
    synchronized_stones = charges.copy()

    # Loop through the stones and synchronize them with their neighbors
    for i in range(1, len(charges) - 1):
        # Calculate the new charge for the current stone
        new_charge = synchronized_stones[i + 1] + synchronized_stones[i - 1] - synchronized_stones[i]

        # Update the charge of the current stone
        synchronized_stones[i] = new_charge

    # Return the synchronized stones
    return synchronized_stones

def main():
    # Read the input data
    n = int(input())
    charges = list(map(int, input().split()))
    target_charges = list(map(int, input().split()))

    # Check if the charges can be synchronized
    if get_synchronized_stones(charges, target_charges) == target_charges:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

