
def get_closest_handsome_number(n):
    # Convert the input number to a list of digits
    digits = [int(digit) for digit in str(n)]
    # Initialize the closest handsome number as the input number
    closest_handsome_number = n
    # Initialize the minimum distance as the absolute value of the difference between the input number and the next handsome number
    min_distance = abs(n - get_next_handsome_number(n))
    # Iterate through all possible handsome numbers
    for i in range(10, 1000000):
        # If the current handsome number is closer to the input number than the current closest handsome number, update the closest handsome number and the minimum distance
        if abs(i - n) < min_distance:
            closest_handsome_number = i
            min_distance = abs(i - n)
    # Return the closest handsome number
    return closest_handsome_number

def get_next_handsome_number(n):
    # Convert the input number to a list of digits
    digits = [int(digit) for digit in str(n)]
    # Initialize the next handsome number as the input number
    next_handsome_number = n
    # Iterate through all possible digits
    for i in range(0, 10):
        # If the current digit is not already in the input number, append it to the end of the input number to form the next handsome number
        if i not in digits:
            next_handsome_number = int(str(n) + str(i))
            break
    # Return the next handsome number
    return next_handsome_number

