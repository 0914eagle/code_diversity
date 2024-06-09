
def get_d(e, e_success, e_failure):
    # Initialize variables
    d = 0
    s = 0
    w = 0

    # Loop until energy reserve is depleted
    while e > 0:
        # Increment weight by 1 kg
        w += 1

        # If weight is greater than or equal to strength, lift succeeds and energy goes down by e_success
        if w >= s:
            e -= e_success
        # If weight is less than strength, lift fails and energy goes down by e_failure
        else:
            e -= e_failure

        # If energy reserve is depleted, break the loop
        if e <= 0:
            break

    # Return the minimum weight such that the score is at least s-d
    return w - s

def main():
    e, e_success, e_failure = map(int, input().split())
    d = get_d(e, e_success, e_failure)
    print(d)

if __name__ == '__main__':
    main()

