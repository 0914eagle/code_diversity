
def solve(A, B, C, D, P, M, G):
    # Calculate the number of minutes in a day
    minutes_in_day = 24 * 60

    # Calculate the number of minutes until the postman arrives
    minutes_until_postman = P * 60

    # Calculate the number of minutes until the milkman arrives
    minutes_until_milkman = M * 60

    # Calculate the number of minutes until the garbage man arrives
    minutes_until_garbage_man = G * 60

    # Initialize the number of aggressive dogs as 0
    num_aggressive_dogs = 0

    # Loop until the postman arrives
    while minutes_until_postman > 0:
        # If the number of aggressive dogs is odd, the dogs will be aggressive
        if num_aggressive_dogs % 2 == 1:
            num_aggressive_dogs += 1

        # Increment the number of minutes
        minutes_until_postman -= 1

        # If the number of minutes is divisible by the duration of an aggressive period, flip the number of aggressive dogs
        if minutes_until_postman % (A + B) == 0:
            num_aggressive_dogs += 1

    # Initialize the number of aggressive dogs as 0
    num_aggressive_dogs = 0

    # Loop until the milkman arrives
    while minutes_until_milkman > 0:
        # If the number of aggressive dogs is odd, the dogs will be aggressive
        if num_aggressive_dogs % 2 == 1:
            num_aggressive_dogs += 1

        # Increment the number of minutes
        minutes_until_milkman -= 1

        # If the number of minutes is divisible by the duration of an aggressive period, flip the number of aggressive dogs
        if minutes_until_milkman % (C + D) == 0:
            num_aggressive_dogs += 1

    # Initialize the number of aggressive dogs as 0
    num_aggressive_dogs = 0

    # Loop until the garbage man arrives
    while minutes_until_garbage_man > 0:
        # If the number of aggressive dogs is odd, the dogs will be aggressive
        if num_aggressive_dogs % 2 == 1:
            num_aggressive_dogs += 1

        # Increment the number of minutes
        minutes_until_garbage_man -= 1

        # If the number of minutes is divisible by the duration of an aggressive period, flip the number of aggressive dogs
        if minutes_until_garbage_man % (A + B) == 0:
            num_aggressive_dogs += 1

    # Return the number of aggressive dogs for each hero
    if num_aggressive_dogs % 2 == 1:
        return "both"
    elif num_aggressive_dogs == 0:
        return "none"
    else:
        return "one"

