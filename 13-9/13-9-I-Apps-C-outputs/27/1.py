
def get_min_chairs(n_guests, left_reqs, right_reqs):
    # Initialize variables
    min_chairs = 0
    current_chair = 1
    previous_guest = 0

    # Loop through each guest
    for i in range(n_guests):
        # Calculate the minimum number of chairs required for this guest
        min_chairs += max(left_reqs[i], right_reqs[i])

        # If the guest has a left requirement that is greater than the current chair number,
        # add the difference to the minimum number of chairs
        if left_reqs[i] > current_chair:
            min_chairs += left_reqs[i] - current_chair

        # If the guest has a right requirement that is greater than the current chair number,
        # add the difference to the minimum number of chairs
        if right_reqs[i] > current_chair:
            min_chairs += right_reqs[i] - current_chair

        # Update the current chair number
        current_chair += 1

        # If the guest has a left requirement that is greater than the current chair number,
        # add the difference to the minimum number of chairs
        if left_reqs[i] > current_chair:
            min_chairs += left_reqs[i] - current_chair

        # If the guest has a right requirement that is greater than the current chair number,
        # add the difference to the minimum number of chairs
        if right_reqs[i] > current_chair:
            min_chairs += right_reqs[i] - current_chair

        # Update the current chair number
        current_chair += 1

    return min_chairs

def main():
    # Read the input
    n_guests = int(input())
    left_reqs = list(map(int, input().split()))
    right_reqs = list(map(int, input().split()))

    # Call the function to get the minimum number of chairs
    min_chairs = get_min_chairs(n_guests, left_reqs, right_reqs)

    # Print the output
    print(min_chairs)

if __name__ == '__main__':
    main()

