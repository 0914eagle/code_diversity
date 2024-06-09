
def get_d(e, e_success, e_failure):
    # Initialize variables
    s = 0
    d = 0
    weight = 0
    success = True

    # While the energy reserve is positive and the weight is less than the maximum conceivable lift
    while e > 0 and weight < 225:
        # Increment the weight by 1
        weight += 1

        # If the weight is greater than or equal to the strength
        if weight >= s:
            # Successful lift
            success = True
            # Decrement the energy reserve by the amount of energy expended in a successful lift
            e -= e_success
        else:
            # Failed lift
            success = False
            # Decrement the energy reserve by the amount of energy expended in a failed lift
            e -= e_failure

        # If the lift was successful and the energy reserve is now zero
        if success and e == 0:
            # Break out of the loop
            break

    # Return the minimum weight such that the score is at least s - d
    return weight - d

def main():
    e, e_success, e_failure = map(int, input().split())
    d = get_d(e, e_success, e_failure)
    print(d)

if __name__ == '__main__':
    main()

