
def get_max_power_of_two(numbers):
    # Initialize a dictionary to store the count of numbers that divide by each power of two
    power_count = {2**i: 0 for i in range(30)}
    # Iterate through the numbers and increment the count for each power of two that divides it
    for num in numbers:
        for i in range(30):
            if num % (2**i) == 0:
                power_count[2**i] += 1
    # Return the power of two with the maximum count
    return max(power_count, key=power_count.get)

