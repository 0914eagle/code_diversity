
def is_possible(area, length):
    
    # Initialize variables
    current_area = 0
    current_length = length

    # Loop through the fencing, adding it to the cage until the area is reached
    while current_area < area:
        # Calculate the area of the current cage
        current_area = current_length * current_length

        # If the current area is greater than the desired area, return False
        if current_area > area:
            return False

        # Subtract the length of the fencing from the total length available
        current_length -= 1

    # If the current area is equal to the desired area, return True
    return current_area == area


# Main program
area = float(input())
length = float(input())

if is_possible(area, length):
    print("Diablo is happy!")
else:
    print("Need more materials!")

