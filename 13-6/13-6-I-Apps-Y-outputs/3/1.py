
def solve(n, r, arr):
    # Sort the array to group together the heaters
    arr.sort()

    # Initialize the number of heaters needed to warm up the whole house
    num_heaters = 0

    # Iterate through the array and count the number of heaters needed
    for i in range(n):
        # If the current element is a heater, increment the number of heaters
        if arr[i] == 1:
            num_heaters += 1

        # If the current element is not a heater, check if it is within the range of a heater
        else:
            # Get the index of the next heater in the array
            next_heater = next((i for i in range(i, n) if arr[i] == 1), n)

            # If there is a heater within the range, do not increment the number of heaters
            if next_heater - i <= r:
                continue

            # Otherwise, increment the number of heaters
            num_heaters += 1

    return num_heaters

