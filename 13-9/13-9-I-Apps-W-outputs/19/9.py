
def can_divide(arr):
    # Calculate the sum of the elements in the array
    sum_arr = sum(arr)
    # Initialize a variable to store the sum of the elements in the first part
    sum_first_part = 0
    # Initialize a variable to store the sum of the elements in the second part
    sum_second_part = 0
    # Iterate through the array
    for i in range(len(arr)):
        # If the sum of the elements in the first part is equal to the sum of the elements in the second part
        if sum_first_part == sum_second_part:
            # Return True
            return True
        # If the sum of the elements in the first part is greater than the sum of the elements in the second part
        elif sum_first_part > sum_second_part:
            # Add the current element to the sum of the elements in the second part
            sum_second_part += arr[i]
        # If the sum of the elements in the first part is less than the sum of the elements in the second part
        else:
            # Add the current element to the sum of the elements in the first part
            sum_first_part += arr[i]
    # If the sum of the elements in the first part is not equal to the sum of the elements in the second part
    return False

def move_element(arr, element, new_position):
    # Remove the element from its current position
    arr.pop(element)
    # Insert the element at the new position
    arr.insert(new_position, element)
    # Return the modified array
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # Call the can_divide function and pass the array as an argument
    if can_divide(arr):
        print("YES")
    else:
        print("NO")

