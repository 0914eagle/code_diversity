
def get_minimum_triples(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize the minimum product and the count of triples
    min_product = arr[0] * arr[1] * arr[2]
    count = 0
    # Loop through the array and find the minimum product
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                # Calculate the product of the current triple
                product = arr[i] * arr[j] * arr[k]
                # If the product is less than the minimum product, update the minimum product and the count of triples
                if product < min_product:
                    min_product = product
                    count = 1
                # If the product is equal to the minimum product, increment the count of triples
                elif product == min_product:
                    count += 1
    return count

