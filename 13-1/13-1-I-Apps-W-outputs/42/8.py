
def is_possible(m, n, days):
    # Initialize a list to store the indices of the stores where Dora bought an integer on each day
    stores_per_day = [[0] * n for _ in range(m)]

    # Populate the list with the indices of the stores where Dora bought an integer on each day
    for day in days:
        for store in day[1:]:
            stores_per_day[day[0] - 1][store - 1] = 1

    # Initialize a list to store the LCMs of the integers bought by Dora on each day
    lcms = [0] * m

    # Calculate the LCMs of the integers bought by Dora on each day
    for day in range(m):
        lcms[day] = calculate_lcm(stores_per_day[day])

    # Initialize a list to store the LCMs of the integers bought by Swiper on each day
    swiper_lcms = [0] * m

    # Calculate the LCMs of the integers bought by Swiper on each day
    for day in range(m):
        swiper_lcms[day] = calculate_lcm(list(filter(lambda x: x == 0, stores_per_day[day])))

    # Check if the LCMs of Dora are strictly greater than the LCMs of Swiper on each day
    for day in range(m):
        if lcms[day] <= swiper_lcms[day]:
            return False

    return True

def calculate_lcm(numbers):
    # Calculate the LCM of a list of numbers
    lcm = 1
    for num in numbers:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

def gcd(a, b):
    # Calculate the greatest common divisor of two numbers
    if b == 0:
        return a
    return gcd(b, a % b)

m, n = map(int, input().split())
days = []
for _ in range(m):
    days.append(list(map(int, input().split())))

if is_possible(m, n, days):
    print("possible")
else:
    print("impossible")

