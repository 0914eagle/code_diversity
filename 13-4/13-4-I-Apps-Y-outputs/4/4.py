
def round_dances(n):
    # Calculate the number of ways to make two round dances with n people
    # where each round dance has n/2 people
    ways = 1
    for i in range(1, n//2):
        ways *= n - i
    return ways

