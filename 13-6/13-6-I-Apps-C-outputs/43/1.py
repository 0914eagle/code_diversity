
def get_expected_payout(num_rows, hole_payouts, bounce_probabilities):
    # Initialize the expected payout to zero
    expected_payout = 0

    # Loop through each hole
    for hole in range(1, num_rows * (num_rows + 1) // 2 + 1):
        # Get the payout for the current hole
        payout = hole_payouts[hole - 1]

        # Loop through each possible bounce
        for bounce in range(4):
            # Get the probability of the ball bouncing to the current bounce
            probability = bounce_probabilities[hole - 1][bounce]

            # If the probability is non-zero, calculate the expected payout for the next hole
            if probability != 0:
                # Get the next hole number
                next_hole = hole + bounce - 2

                # If the next hole is valid, calculate the expected payout for that hole
                if next_hole > 0 and next_hole <= num_rows * (num_rows + 1) // 2:
                    expected_payout += probability * get_expected_payout(num_rows, hole_payouts, bounce_probabilities)

    # Return the expected payout for the current hole
    return expected_payout + payout

def main():
    # Read the input
    num_rows = int(input())
    hole_payouts = list(map(int, input().split()))
    bounce_probabilities = []
    for _ in range(num_rows):
        bounce_probabilities.append(list(map(float, input().split())))

    # Calculate the expected payout
    expected_payout = get_expected_payout(num_rows, hole_payouts, bounce_probabilities)

    # Print the expected payout
    print(expected_payout)

if __name__ == '__main__':
    main()

