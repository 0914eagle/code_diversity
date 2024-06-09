
def solve(B, k, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy B bolts
    min_bolts_required = {0: 0}
    # Loop through each company
    for i in range(k):
        # Get the number of types of packages and their sizes for the current company
        l, *sizes = companies[i]
        # Loop through each type of package
        for j in range(l):
            # Get the size of the current package
            size = sizes[j]
            # Check if the current package is greater than or equal to the number of bolts required
            if size >= min_bolts_required.get(B, float('inf')):
                # If it is, update the minimum number of bolts required to buy B bolts
                min_bolts_required[B] = size
                # Break out of the loop
                break
        # If the minimum number of bolts required has been updated, break out of the loop
        if min_bolts_required.get(B, float('inf')) != float('inf'):
            break
    # Check if the minimum number of bolts required is infinite, which means it is impossible to buy B bolts
    if min_bolts_required.get(B, float('inf')) == float('inf'):
        return "impossible"
    # Otherwise, return the minimum number of bolts required
    return min_bolts_required[B]

