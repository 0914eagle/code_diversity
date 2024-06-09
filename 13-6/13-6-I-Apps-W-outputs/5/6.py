
def get_min_triples(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum product and the count of triples
    min_prod = arr[0] * arr[1] * arr[2]
    count = 0
    # Loop through the array and check if the product of any three consecutive elements is less than the minimum product
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                prod = arr[i] * arr[j] * arr[k]
                if prod < min_prod:
                    min_prod = prod
                    count += 1
    return count

