
def get_min_sum(arr):
    # Initialize variables
    n = len(arr)
    sum_odd = 0
    sum_even = 0
    parity = 0
    deleted_elements = []
    
    # Iterate through the array
    for i in range(n):
        # If the current element is odd
        if arr[i] % 2 == 1:
            # If the current parity is even
            if parity == 0:
                # Add the current element to the sum of even elements
                sum_even += arr[i]
                # Set the current parity to odd
                parity = 1
            # If the current parity is odd
            else:
                # Add the current element to the sum of odd elements
                sum_odd += arr[i]
                # Set the current parity to even
                parity = 0
        # If the current element is even
        else:
            # If the current parity is even
            if parity == 0:
                # Add the current element to the sum of even elements
                sum_even += arr[i]
                # Set the current parity to odd
                parity = 1
            # If the current parity is odd
            else:
                # Add the current element to the sum of odd elements
                sum_odd += arr[i]
                # Set the current parity to even
                parity = 0
    
    # If the sum of odd elements is less than the sum of even elements
    if sum_odd < sum_even:
        # Return the sum of odd elements
        return sum_odd
    # If the sum of even elements is less than the sum of odd elements
    else:
        # Return the sum of even elements
        return sum_even

if __name__ == '__main__':
    arr = [int(input()) for _ in range(int(input()))]
    print(get_min_sum(arr))

