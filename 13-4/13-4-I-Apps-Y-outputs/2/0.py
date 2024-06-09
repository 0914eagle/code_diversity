
def is_possible(area, fencing_length):
    # Calculate the minimum area of the cage
    min_area = fencing_length ** 2

    # Check if the area is greater than or equal to the minimum area
    if area >= min_area:
        return True
    else:
        return False

# Main function
if __name__ == '__main__':
    # Read the input
    area, fencing_length = map(float, input().split())

    # Check if it is possible to build the cage
    if is_possible(area, fencing_length):
        print("Diablo is happy!")
    else:
        print("Need more materials!")

