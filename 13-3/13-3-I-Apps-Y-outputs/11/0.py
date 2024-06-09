
def solve(N, T):
    # Find the least common multiple (LCM) of all the times
    lcm = T[0]
    for i in range(1, N):
        lcm = lcm_of_two_numbers(lcm, T[i])

    # Return the LCM as the required answer
    return lcm

# Function to find the least common multiple of two numbers
def lcm_of_two_numbers(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if(greater % x == 0 and greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

