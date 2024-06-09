
def get_score(s, e, e_success, e_failure):
    # Initialize variables
    weight = 25
    score = 0
    energy = e

    # Loop until energy is depleted
    while energy > 0:
        # Check if weight is within the maximum conceivable lift
        if weight <= 225:
            # Check if weight is within the strength limit
            if weight <= s:
                # Successful lift
                score = weight
                energy -= e_success
            else:
                # Failed lift
                energy -= e_failure
        else:
            # Break the loop if the weight is greater than the maximum conceivable lift
            break
        # Increment the weight by 2.5 kg
        weight += 2.5

    # Return the score
    return score

def get_d(e, e_success, e_failure):
    # Initialize variables
    s = 0
    d = 0

    # Loop until the optimal score is found
    while True:
        # Get the score for the current strength limit
        score = get_score(s, e, e_success, e_failure)
        # Check if the score is greater than the current strength limit minus the minimum weight
        if score >= s - d:
            # Increment the minimum weight
            d += 2.5
        else:
            # Break the loop if the score is less than the current strength limit minus the minimum weight
            break
        # Increment the strength limit
        s += 2.5

    # Return the minimum weight
    return d

if __name__ == '__main__':
    e, e_success, e_failure = map(int, input().split())
    print(get_d(e, e_success, e_failure))

