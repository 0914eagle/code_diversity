
def get_maximal_product(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the product of the elements as 1
    product = 1
    # Loop through the array and calculate the product of the elements
    for i in range(len(arr)):
        product *= arr[i]
    # Return the product of the elements
    return product

def get_maximal_product_with_operation(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the product of the elements as 1
    product = 1
    # Loop through the array and calculate the product of the elements
    for i in range(len(arr)):
        product *= arr[i]
        # If the element is negative, multiply it by -1 and add 1 to it
        if arr[i] < 0:
            arr[i] = -arr[i] - 1
    # Return the product of the elements
    return product

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(get_maximal_product_with_operation(arr))

