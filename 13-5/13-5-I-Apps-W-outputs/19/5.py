
def get_maximum_product(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum product to 1
    max_product = 1
    # Iterate through the array and calculate the product of positive numbers
    for i in range(len(arr)):
        if arr[i] > 0:
            max_product *= arr[i]
    # Return the maximum product
    return max_product

def change_array(arr):
    # Initialize a new array to store the changed array
    new_arr = []
    # Iterate through the array and change the sign of negative numbers
    for i in range(len(arr)):
        if arr[i] < 0:
            new_arr.append(-arr[i] - 1)
        else:
            new_arr.append(arr[i])
    # Return the changed array
    return new_arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # Get the maximum product of the original array
    max_product = get_maximum_product(arr)
    # Change the array and get the maximum product of the changed array
    changed_arr = change_array(arr)
    changed_product = get_maximum_product(changed_arr)
    # If the maximum product of the changed array is greater than the maximum product of the original array, print the changed array
    if changed_product > max_product:
        print(*changed_arr)
    # Otherwise, print the original array
    else:
        print(*arr)

