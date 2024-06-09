
def get_min_triples(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize variables to keep track of the minimum product and its indices
    min_product = arr[0] * arr[1] * arr[2]
    min_indices = [0, 1, 2]
    # Iterate over the array
    for i in range(len(arr) - 2):
        # Calculate the product of the current element with the two following elements
        product = arr[i] * arr[i + 1] * arr[i + 2]
        # If the product is less than the minimum product, update the minimum product and its indices
        if product < min_product:
            min_product = product
            min_indices = [i, i + 1, i + 2]
    # Return the minimum product and its indices
    return min_product, min_indices

