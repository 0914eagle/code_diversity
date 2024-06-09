
def is_possible(m, n, days):
    # Initialize a list to store the indices of the stores where Dora bought an integer on each day
    stores_per_day = [[0] * n for _ in range(m)]

    # Iterate over each day
    for i in range(m):
        # Get the indices of the stores where Dora bought an integer on the current day
        stores_per_day[i] = [int(x) for x in input().split()[1:]]

    # Initialize a set to store the indices of the stores where Dora and Swiper bought integers on each day
    stores_set = set()

    # Iterate over each day
    for i in range(m):
        # Get the indices of the stores where Dora and Swiper bought integers on the current day
        stores_set |= set(stores_per_day[i])

    # Check if the number of stores where Dora and Swiper bought integers is equal to the total number of stores
    if len(stores_set) == n:
        return "impossible"

    # Initialize a list to store the LCMs of the integers bought by Dora and Swiper on each day
    lcms = [0] * m

    # Iterate over each day
    for i in range(m):
        # Get the indices of the stores where Dora and Swiper bought integers on the current day
        stores = stores_per_day[i]

        # Initialize a list to store the integers bought by Dora and Swiper on the current day
        integers = [0] * (n - len(stores_set))

        # Iterate over each store
        for j in range(n):
            # Check if the current store is not in the set of stores where Dora and Swiper bought integers
            if j not in stores_set:
                # Add the integer from the current store to the list of integers bought by Dora and Swiper
                integers[j - len(stores_set)] = j + 1

        # Calculate the LCM of the integers bought by Dora and Swiper on the current day
        lcms[i] = get_lcm(integers)

    # Initialize a flag to indicate if Dora beat Swiper on each day
    is_possible = True

    # Iterate over each day
    for i in range(m):
        # Check if the LCM of the integers bought by Dora is strictly greater than the LCM of the integers bought by Swiper on the current day
        if lcms[i] <= lcms[(i + 1) % m]:
            # Set the flag to False
            is_possible = False
            break

    # Return "possible" if Dora beat Swiper on each day, otherwise return "impossible"
    return "possible" if is_possible else "impossible"

def get_lcm(integers):
    # Initialize the LCM to the first integer
    lcm = integers[0]

    # Iterate over each integer
    for i in range(1, len(integers)):
        # Calculate the LCM of the current integer and the previous LCM
        lcm = lcm * integers[i] // gcd(lcm, integers[i])

    # Return the LCM
    return lcm

def gcd(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a

    # Recursive case: calculate the GCD of b and the remainder of a divided by b
    return gcd(b, a % b)

m, n = map(int, input().split())
days = [0] * m
for i in range(m):
    days[i] = input()
print(is_possible(m, n, days))

