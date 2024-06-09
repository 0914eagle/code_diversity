
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

def change_array(arr):
    # Initialize a new array to store the changed elements
    new_arr = []
    # Loop through the array and change the elements as specified in the problem
    for i in range(len(arr)):
        if arr[i] < 0:
            new_arr.append(-arr[i] - 1)
        else:
            new_arr.append(-arr[i] - 1)
    # Return the changed array
    return new_arr

def main():
    # Accept the number of integers in the array as input
    n = int(input())
    # Accept the integers in the array as input
    arr = list(map(int, input().split()))
    # Call the function to get the maximal product of the elements
    product = get_maximal_product(arr)
    # Call the function to change the array as specified in the problem
    new_arr = change_array(arr)
    # Print the array with the maximal possible product of elements
    print(*new_arr)

if __name__ == '__main__':
    main()

