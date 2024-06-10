
def get_unique_sums(beauties, k):
    # Sort the beauties in non-decreasing order
    beauties.sort()
    # Initialize the list of sums with the first beauty
    sums = [beauties[0]]
    # Iterate over the remaining beauties
    for beauty in beauties[1:]:
        # Check if the sum of the current beauty with any of the existing sums is less than or equal to k
        for i in range(len(sums)):
            if sums[i] + beauty <= k:
                # If so, add the current beauty to the sum and break the loop
                sums.append(sums[i] + beauty)
                break
        else:
            # If we reach this point, it means that we could not find a suitable sum, so we return None
            return None
    return sums

def get_detachments(beauties, k):
    # Get a list of unique sums
    sums = get_unique_sums(beauties, k)
    if sums is None:
        return None
    # Initialize the list of detachments
    detachments = []
    # Iterate over the sums
    for sum in sums:
        # Get the indices of the soldiers with the current sum
        indices = [i for i, beauty in enumerate(beauties) if beauty == sum]
        # Add the indices to the list of detachments
        detachments.append(indices)
    return detachments

def main():
    n, k = map(int, input().split())
    beauties = list(map(int, input().split()))
    detachments = get_detachments(beauties, k)
    if detachments is None:
        print("Impossible")
    else:
        for detachment in detachments:
            print(len(detachment), *detachment)

if __name__ == '__main__':
    main()

