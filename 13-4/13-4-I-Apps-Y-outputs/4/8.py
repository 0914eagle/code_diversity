
def round_dances(n):
    # Calculate the number of ways to make two round dances with n people
    # Each round dance consists of exactly n/2 people
    # Each person should belong to exactly one of these two round dances
    # Return the number of ways to make two round dances
    ways = 0
    
    # Iterate over all possible combinations of people for the first round dance
    for i in range(1, n+1):
        # Calculate the number of ways to make the second round dance
        # with the remaining people and the current first round dance
        ways += round_dances_helper(n-i, i)
    
    return ways

def round_dances_helper(n, m):
    # Calculate the number of ways to make a round dance with n people
    # and the first person is the mth person
    # Return the number of ways to make the round dance
    if n == 0:
        # Base case: no people left, only one way to make the round dance
        return 1
    else:
        # Recursive case: calculate the number of ways to make the round dance
        # with the remaining people and the current first person
        return n * round_dances_helper(n-1, m)

n = int(input())
print(round_dances(n))

