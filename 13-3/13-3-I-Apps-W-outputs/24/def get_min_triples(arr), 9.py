
def get_min_triples(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum product and the count of triples
    min_product = arr[0] * arr[1] * arr[2]
    count = 0
    # Loop through the array and find the triples with the minimum product
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                product = arr[i] * arr[j] * arr[k]
                if product < min_product:
                    min_product = product
                    count = 1
                elif product == min_product:
                    count += 1
    return count

