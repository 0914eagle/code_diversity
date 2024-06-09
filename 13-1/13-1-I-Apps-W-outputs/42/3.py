
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

        # Add the numbers bought by Dora and Swiper to their respective lists
        dora_numbers[day] = [days[day][0]] + [days[day][i] for i in dora_indices]
        swiper_numbers[day] = [days[day][i] for i in swiper_indices]

    # Initialize a flag to indicate whether it is possible for Dora to beat Swiper
    possible = True

    # Iterate over the days
    for day in range(m):
        # Get the LCM of the numbers bought by Dora on the current day
        dora_lcm = get_lcm(dora_numbers[day])
        # Get the LCM of the numbers bought by Swiper on the current day
        swiper_lcm = get_lcm(swiper_numbers[day])

        # If the LCM of Dora's numbers is less than or equal to the LCM of Swiper's numbers, set the possible flag to False
        if dora_lcm <= swiper_lcm:
            possible = False
            break

    # Return the possible flag
    return "possible" if possible else "impossible"

# Function to get the least common multiple of a list of numbers
def get_lcm(numbers):
    # Initialize the least common multiple to the first number in the list
    lcm = numbers[0]

    # Iterate over the remaining numbers in the list
    for number in numbers[1:]:
        # Update the least common multiple to the least common multiple of the current number and the previous least common multiple
        lcm = lcm * number // gcd(lcm, number)

    # Return the least common multiple
    return lcm

# Function to calculate the greatest common divisor of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function with the sample input
m, n = map(int, input().split())
days = [list(map(int, input().split())) for _ in range(m)]
print(is_possible(m, n, days))

