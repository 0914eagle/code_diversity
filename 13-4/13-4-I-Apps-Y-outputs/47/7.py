
def solve(l, n):
    # Initialize the number of rolls as 1
    k = 1
    # Loop until the length of the roll is greater than or equal to the number of centimeters needed
    while l < n:
        # Increase the number of rolls by 1
        k += 1
        # Calculate the new length of the roll
        l += l
    # Return the smallest number of rolls that can prevent crises from happening
    return k

