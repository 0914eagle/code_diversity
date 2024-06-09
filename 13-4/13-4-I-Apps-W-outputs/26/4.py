
def get_d(e, e_success, e_failure):
    # Initialize variables
    s = 0
    d = 0
    weight = 0

    # While there is still energy left
    while e > 0:
        # Try to lift the maximum weight
        weight = 225
        if s >= weight:
            # Successful lift
            e -= e_success
            s -= weight
            d = max(d, weight - s)
        else:
            # Failed lift
            e -= e_failure
            s = 0

        # Decrease the weight by 10 kg
        weight -= 10

    # Return the minimum weight such that the score is at least s-d
    return d

def main():
    e, e_success, e_failure = map(int, input().split())
    d = get_d(e, e_success, e_failure)
    print(d)

if __name__ == '__main__':
    main()

