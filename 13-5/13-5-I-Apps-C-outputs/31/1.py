
def solve(B, k, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack
    # from each company, and the corresponding company and pack size
    min_bolts_required = {}
    for i in range(k):
        min_bolts_required[i] = (float('inf'), 0, 0)

    # Loop through each company and its packs
    for i, company in enumerate(companies):
        for j, pack in enumerate(company):
            # If the pack size is greater than or equal to the number of bolts needed,
            # and the number of bolts required is less than the current minimum,
            # update the minimum number of bolts required and the corresponding company and pack size
            if pack >= B and pack < min_bolts_required[i][0]:
                min_bolts_required[i] = (pack, i, j)

    # If the minimum number of bolts required is infinite, it means it's impossible to buy a pack with the given number of bolts
    if min_bolts_required[k-1][0] == float('inf'):
        return "impossible"

    # Otherwise, return the smallest pack size that satisfies the minimum number of bolts required
    return min_bolts_required[k-1][1]

