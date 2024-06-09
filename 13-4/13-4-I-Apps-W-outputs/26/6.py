
def get_d(e, e_success, e_failure):
    # Initialize variables
    s = 0
    d = 0
    weight = 0
    success = True

    # While the energy reserve is positive and the weight is less than the maximum conceivable lift
    while e > 0 and weight < 225:
        # Increment the weight by the current strength
        weight += s

        # If the weight is greater than the maximum conceivable lift, set the weight to the maximum conceivable lift
        if weight > 225:
            weight = 225

        # If the weight is less than the empty bar, set the weight to the empty bar
        if weight < 25:
            weight = 25

        # If the weight is greater than the strength, set the success flag to False
        if weight > s:
            success = False

        # If the success flag is True, subtract the energy expended in a successful lift from the energy reserve
        if success:
            e -= e_success
        # Otherwise, subtract the energy expended in a failed lift from the energy reserve
        else:
            e -= e_failure

        # If the energy reserve is now negative, set the success flag to False
        if e < 0:
            success = False

        # If the success flag is True, add the weight to the current strength
        if success:
            s += weight

        # Increment the weight by 25 kg
        weight += 25

    # Return the minimum weight such that the score is at least s - d
    return s - d

if __name__ == '__main__':
    e, e_success, e_failure = map(int, input().split())
    print(get_d(e, e_success, e_failure))

