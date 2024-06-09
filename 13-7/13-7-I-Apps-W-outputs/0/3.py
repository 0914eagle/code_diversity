
def max_power(numbers):
    # Find the maximum power of 2 that divides any of the numbers
    max_power = 0
    for num in numbers:
        power = 0
        while num % 2 == 0:
            num //= 2
            power += 1
        max_power = max(max_power, power)
    
    # Count the number of numbers that divide by the maximum power
    count = 0
    for num in numbers:
        if num % 2**max_power == 0:
            count += 1
    
    return max_power, count

