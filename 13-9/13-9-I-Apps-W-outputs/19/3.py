
def can_divide_array(a):
    # Calculate the sum of the elements in the array
    sum_a = sum(a)
    # Initialize a variable to keep track of the sum of the elements in the first part of the array
    sum_first_part = 0
    # Initialize a variable to keep track of the sum of the elements in the second part of the array
    sum_second_part = 0
    # Initialize a variable to keep track of the number of elements in the first part of the array
    count_first_part = 0
    # Initialize a variable to keep track of the number of elements in the second part of the array
    count_second_part = len(a)
    # Initialize a variable to keep track of the index of the element to move
    index_to_move = 0
    # Initialize a variable to keep track of the new position of the element to move
    new_position = 0

    # Loop through the array and calculate the sum of the elements in the first part of the array
    for i in range(len(a)):
        sum_first_part += a[i]
        count_first_part += 1
        if sum_first_part == sum_a // 2:
            break

    # Loop through the array in reverse and calculate the sum of the elements in the second part of the array
    for i in range(len(a) - 1, -1, -1):
        sum_second_part += a[i]
        count_second_part -= 1
        if sum_second_part == sum_a // 2:
            break

    # Check if the sum of the elements in the first part of the array is equal to the sum of the elements in the second part of the array
    if sum_first_part == sum_second_part:
        return True

    # Check if the sum of the elements in the first part of the array is greater than the sum of the elements in the second part of the array
    if sum_first_part > sum_second_part:
        # Find the element to move by subtracting the sum of the elements in the first part of the array from the sum of the elements in the array
        index_to_move = sum_a - sum_first_part
        # Find the new position of the element to move by subtracting the number of elements in the first part of the array from the length of the array
        new_position = len(a) - count_first_part
        # Move the element to the new position
        a.insert(new_position, a.pop(index_to_move))
        # Return True if the sum of the elements in the first part of the array is equal to the sum of the elements in the second part of the array after moving the element
        return sum_first_part == sum_second_part

    # Check if the sum of the elements in the first part of the array is less than the sum of the elements in the second part of the array
    if sum_first_part < sum_second_part:
        # Find the element to move by subtracting the sum of the elements in the second part of the array from the sum of the elements in the array
        index_to_move = sum_a - sum_second_part
        # Find the new position of the element to move by subtracting the number of elements in the second part of the array from the length of the array
        new_position = len(a) - count_second_part
        # Move the element to the new position
        a.insert(new_position, a.pop(index_to_move))
        # Return True if the sum of the elements in the first part of the array is equal to the sum of the elements in the second part of the array after moving the element
        return sum_first_part == sum_second_part

    # If the sum of the elements in the first part of the array is not equal to the sum of the elements in the second part of the array, return False
    return False

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if can_divide_array(a) else "NO")

if __name__ == '__main__':
    main()

