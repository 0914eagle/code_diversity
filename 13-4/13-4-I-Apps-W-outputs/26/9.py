
def get_optimal_score(e, e_success, e_failure):
    # Initialize variables
    s = 0
    w = 25
    d = 0

    # While there is still energy left and the weight is less than the maximum conceivable lift
    while e > 0 and w < 225:
        # If the weight is greater than or equal to the strength
        if w >= s:
            # Successful lift, decrease energy by e_success
            e -= e_success
            # Increase strength by the weight
            s += w
            # Increase the optimal score by the weight
            d += w
        # If the weight is less than the strength
        else:
            # Failed lift, decrease energy by e_failure
            e -= e_failure
            # Increase the weight by 25 kg
            w += 25

    # Return the optimal score
    return d

def main():
    e, e_success, e_failure = map(int, input().split())
    print(get_optimal_score(e, e_success, e_failure))

if __name__ == '__main__':
    main()

