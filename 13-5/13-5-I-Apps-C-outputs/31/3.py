
def get_smallest_pack_size(B, k, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack of size i
    min_bolts_required = {}
    for i in range(1, B+1):
        min_bolts_required[i] = i

    # Iterate over the companies and their packages
    for company in companies:
        for package in company:
            # Check if the package size is less than or equal to the minimum number of bolts required
            if package <= min_bolts_required[package]:
                # If it is, update the minimum number of bolts required for this package size
                min_bolts_required[package] = package
            else:
                # If it's not, check if the package size is less than the minimum number of bolts required but greater than the next smallest package size
                if package < min_bolts_required[package+1]:
                    # If it is, update the minimum number of bolts required for this package size
                    min_bolts_required[package] = package

    # Return the smallest package size that contains at least the number of bolts required
    return min(min_bolts_required, key=min_bolts_required.get)

