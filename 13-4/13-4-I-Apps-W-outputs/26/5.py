
def get_d(e, e_success, e_failure):
    # Initialize variables
    s = 0
    d = 0
    weight = 25
    max_weight = 225

    # While we have enough energy to lift more
    while e > 0:
        # If we can lift the current weight
        if s >= weight:
            # Successful lift
            e -= e_success
            s -= weight
            d += weight
        else:
            # Failed lift
            e -= e_failure

        # Increase weight by 25 kg
        weight += 25

        # If we have reached the maximum weight, break
        if weight > max_weight:
            break

    # Return the minimum weight such that we can guarantee a score of at least s-d
    return d

def main():
    e, e_success, e_failure = map(int, input().split())
    print(get_d(e, e_success, e_failure))

if __name__ == '__main__':
    main()

