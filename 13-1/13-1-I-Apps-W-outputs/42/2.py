
def is_possible(m, n, days):
    # Initialize a list to store the numbers bought by Dora on each day
    dora_numbers = [[] for _ in range(m)]
    # Initialize a list to store the numbers bought by Swiper on each day
    swiper_numbers = [[] for _ in range(m)]

    # Iterate over the days
    for day in range(m):
        # Get the indices of the stores where Dora bought an integer on the current day
        dora_indices = days[day][1:]
        # Get the indices of the stores where Swiper bought an integer on the current day
        swiper_indices = [i for i in range(1, n + 1) if i not in dora_indices]

        # Add the integers bought by Dora on the current day to the list
        dora_numbers[day] = [days[day][0]] + [days[day][i] for i in dora_indices]
        # Add the integers bought by Swiper on the current day to the list
        swiper_numbers[day] = [days[day][i] for i in swiper_indices]

    # Iterate over the days
    for day in range(m):
        # Get the LCM of the integers bought by Dora on the current day
        dora_lcm = get_lcm(dora_numbers[day])
        # Get the LCM of the integers bought by Swiper on the current day
        swiper_lcm = get_lcm(swiper_numbers[day])

        # If the LCM of Dora's integers is not greater than the LCM of Swiper's integers, return False
        if dora_lcm <= swiper_lcm:
            return False

    # If all days have been processed and no condition has been violated, return True
    return True

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

# Test the function with the sample input
m, n = map(int, input().split())
days = [list(map(int, input().split())) for _ in range(m)]
print("possible" if is_possible(m, n, days) else "impossible")

