
def max_power_of_two(numbers):
    # Initialize variables
    max_power = 0
    count = 0

    # Iterate through the numbers
    for num in numbers:
        # Find the maximum power of two that divides the number
        power = 0
        while num % 2 == 0:
            num //= 2
            power += 1

        # Update the maximum power and count
        if power > max_power:
            max_power = power
            count = 1
        elif power == max_power:
            count += 1

    return max_power, count

