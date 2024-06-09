
def get_max_divisible(A, K):
    # Sort the array in non-decreasing order
    A.sort()
    # Initialize the maximum divisible number as the smallest number in the array
    max_divisible = A[0]
    # Loop through each number in the array
    for i in range(1, len(A)):
        # If the current number is not a multiple of the maximum divisible number, we cannot make it a multiple
        if A[i] % max_divisible != 0:
            # Find the smallest number that is a multiple of the current number and is less than or equal to the maximum divisible number
            multiple = (max_divisible // A[i]) * A[i]
            # If the smallest number is greater than the current number, we can make the current number the maximum divisible number
            if multiple > A[i]:
                max_divisible = A[i]
            # If the smallest number is less than or equal to the current number, we cannot make the current number the maximum divisible number
            else:
                return max_divisible
    # If we reach the end of the array, return the maximum divisible number
    return max_divisible

