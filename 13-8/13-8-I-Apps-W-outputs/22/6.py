
def solve(n, c, t):
    # Initialize a dictionary to store the charges of Grigory's stones
    charges = {i: c[i-1] for i in range(1, n+1)}
    # Initialize a set to store the indices of the stones that have been synchronized
    synchronized = set()
    # Loop through each stone and check if it can be synchronized with its neighbors
    for i in range(1, n+1):
        # If the stone has already been synchronized, skip it
        if i in synchronized:
            continue
        # If the stone does not have the required charge, try synchronizing it with its neighbors
        if charges[i] != t[i-1]:
            # If the stone has a neighbor with the required charge, synchronize it with that neighbor
            if i-1 in charges and charges[i-1] == t[i-1]:
                synchronized.add(i-1)
                charges[i] = charges[i-1]
            elif i+1 in charges and charges[i+1] == t[i-1]:
                synchronized.add(i+1)
                charges[i] = charges[i+1]
            # If neither neighbor has the required charge, return "No"
            else:
                return "No"
    # If all stones have the required charge, return "Yes"
    return "Yes"

