
def solve(B, k, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a package of a certain size
    min_bolts = {}
    # Initialize a dictionary to store the number of bolts in a package of a certain size
    num_bolts = {}
    # Loop through each company
    for i in range(k):
        # Loop through each package type offered by the company
        for j in range(companies[i][0]):
            # Get the size of the package
            size = companies[i][j+1]
            # If the package is the smallest size that contains at least B bolts, return it
            if size >= B:
                return size
            # If the package is not the smallest size that contains at least B bolts, add it to the dictionary of minimum number of bolts required to buy a package of that size
            if size not in min_bolts or min_bolts[size] > B:
                min_bolts[size] = B
            # Add the number of bolts in the package to the dictionary of number of bolts in a package of that size
            num_bolts[size] = companies[i][j+1]
    
    # If no package contains at least B bolts, return "impossible"
    return "impossible"

