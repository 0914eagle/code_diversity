
def is_possible(m, n, days):
    # Initialize a list to store the indices of the stores where Dora bought an integer on each day
    stores_per_day = [[0] * n for _ in range(m)]

    # Populate the list with the indices of the stores where Dora bought an integer on each day
    for day in days:
        for store in day[1:]:
            stores_per_day[day[0] - 1][store - 1] = 1

    # Initialize a list to store the least common multiples of the integers bought by Dora on each day
    lcms = [0] * m

    # Calculate the least common multiple of the integers bought by Dora on each day
    for day in range(m):
        lcms[day] = calculate_lcm(stores_per_day[day])

    # Initialize a list to store the least common multiples of the integers bought by Swiper on each day
    swiper_lcms = [0] * m

    # Calculate the least common multiple of the integers bought by Swiper on each day
    for day in range(m):
        swiper_lcms[day] = calculate_lcm([1 - x for x in stores_per_day[day]])

    # Check if the least common multiple of the integers bought by Dora is strictly greater than the least common multiple of the integers bought by Swiper on each day
    for day in range(m):
        if lcms[day] <= swiper_lcms[day]:
            return "impossible"

    return "possible"

def calculate_lcm(numbers):
    # Initialize the least common multiple to the first number
    lcm = numbers[0]

    # Iterate through the remaining numbers and calculate their least common multiple
    for number in numbers[1:]:
        lcm = lcm * number // gcd(lcm, number)

    return lcm

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

m, n = map(int, input().split())
days = []
for _ in range(m):
    days.append(list(map(int, input().split())))

print(is_possible(m, n, days))

