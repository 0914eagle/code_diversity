
def is_possible(m, n, days):
    # Initialize a list to store the numbers bought by Dora on each day
    dora_numbers = [[] for _ in range(m)]
    # Initialize a list to store the numbers bought by Swiper on each day
    swiper_numbers = [[] for _ in range(m)]

    # Iterate over the days
    for day in range(m):
        # Get the indices of the stores where Dora bought an integer on the current day
        dora_stores = days[day][1:]
        # Get the indices of the stores where Swiper bought an integer on the current day
        swiper_stores = [store for store in range(1, n + 1) if store not in dora_stores]

        # Add the integers bought by Dora on the current day to the list
        dora_numbers[day].extend(days[day][1:])
        # Add the integers bought by Swiper on the current day to the list
        swiper_numbers[day].extend(swiper_stores)

    # Iterate over the days
    for day in range(m):
        # Get the LCM of the integers bought by Dora on the current day
        dora_lcm = get_lcm(dora_numbers[day])
        # Get the LCM of the integers bought by Swiper on the current day
        swiper_lcm = get_lcm(swiper_numbers[day])

        # If the LCM of Dora's integers is not greater than the LCM of Swiper's integers, return "impossible"
        if dora_lcm <= swiper_lcm:
            return "impossible"

    # If all days have been processed and no "impossible" condition has been encountered, return "possible"
    return "possible"

def get_lcm(numbers):
    # Initialize the LCM to the first number
    lcm = numbers[0]
    # Iterate over the remaining numbers
    for number in numbers[1:]:
        # Update the LCM to the least common multiple of the current LCM and the current number
        lcm = lcm * number // gcd(lcm, number)
    # Return the LCM
    return lcm

def gcd(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: return the GCD of b and the remainder of a divided by b
    return gcd(b, a % b)

m, n = map(int, input().split())
days = []
for _ in range(m):
    days.append(list(map(int, input().split())))

print(is_possible(m, n, days))

