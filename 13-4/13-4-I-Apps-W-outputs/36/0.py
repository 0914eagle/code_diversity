
def get_max_power_of_two(numbers):
    max_power = 0
    count = 0
    for num in numbers:
        power = 0
        while num % 2 == 0:
            num //= 2
            power += 1
        if power > max_power:
            max_power = power
        if power > 0:
            count += 1
    return max_power, count

