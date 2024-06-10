
def get_paint_required(digits):
    # Calculate the total amount of paint required for the given digits
    total_paint = 0
    for digit in digits:
        total_paint += digit
    return total_paint

def get_max_number(paint, digits):
    # Initialize the maximum number as 0
    max_number = 0
    
    # Iterate through the digits and check if the current digit can be used
    for digit in digits:
        # Check if the current digit can be used with the available paint
        if digit <= paint:
            # Update the maximum number by adding the current digit
            max_number = max_number * 10 + digit
            # Update the available paint by subtracting the current digit
            paint -= digit
    
    # Return the maximum number
    return max_number

def main():
    # Read the input
    v = int(input())
    digits = [int(x) for x in input().split()]
    
    # Calculate the total amount of paint required
    paint = get_paint_required(digits)
    
    # Check if the available paint is enough to write any number
    if paint == 0:
        print(-1)
    else:
        # Find the maximum number that can be written
        max_number = get_max_number(paint, digits)
        print(max_number)

if __name__ == '__main__':
    main()

