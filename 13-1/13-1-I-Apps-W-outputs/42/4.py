
def is_possible(m, n, days):
    # Initialize a list to store the indices of the stores where Dora bought an integer on each day
    stores_per_day = [[0] * n for _ in range(m)]

    # Iterate over each day
    for i in range(m):
        # Get the indices of the stores where Dora bought an integer on the current day
        stores_per_day[i] = [int(x) for x in input().split()[1:]]

    # Initialize a set to store the indices of the stores where Dora and Swiper bought integers on the same day
    common_stores = set()

    # Iterate over each day
    for i in range(m):
        # Get the indices of the stores where Dora and Swiper bought integers on the current day
        common_stores |= set(stores_per_day[i])

    # Initialize a list to store the values of a_i
    a = [0] * n

    # Iterate over each store
    for i in range(n):
        # If the store is not in the set of common stores, set a_i to 1
        if i not in common_stores:
            a[i] = 1

    # Initialize a list to store the least common multiples of the integers bought by Dora and Swiper on each day
    lcm = [0] * m

    # Iterate over each day
    for i in range(m):
        # Get the indices of the stores where Dora and Swiper bought integers on the current day
        stores = stores_per_day[i]

        # Initialize a list to store the integers bought by Dora and Swiper on the current day
        integers = [a[j] for j in stores]

        # Calculate the least common multiple of the integers bought by Dora and Swiper on the current day
        lcm[i] = get_lcm(integers)

    # Initialize a boolean to indicate if Dora beat Swiper on every day
    possible = True

    # Iterate over each day
    for i in range(m):
        # If the least common multiple of the integers bought by Dora is not strictly greater than the least common multiple of the integers bought by Swiper on the current day, set possible to False
        if lcm[i] <= lcm[i-1]:
            possible = False
            break

    # Return possible
    return "possible" if possible else "impossible"

def get_lcm(integers):
    # Initialize the least common multiple to the first integer
    lcm = integers[0]

    # Iterate over each integer
    for i in integers[1:]:
        # Calculate the least common multiple of the current integer and the previous least common multiple
        lcm = lcm * i // gcd(lcm, i)

    # Return the least common multiple
    return lcm

def gcd(a, b):
    # While b is not 0
    while b != 0:
        # a is the new b
        a, b = b, a % b

    # Return a
    return a

m, n = map(int, input().split())
days = [input() for _ in range(m)]
print(is_possible(m, n, days))

