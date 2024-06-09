
import sys

def count_seating_arrangements(n, current_seats, desired_seats):
    # Initialize a list to store the possible assignments
    assignments = []

    # Iterate over the current and desired seats
    for i in range(n):
        # If the current seat is not the desired seat, add the current seat to the assignments list
        if current_seats[i] != desired_seats[i]:
            assignments.append(current_seats[i])

    # Return the number of possible assignments, modulo 1000000007
    return len(assignments) % 1000000007

n = int(input())
current_seats = []
desired_seats = []

# Iterate over the number of engineers
for i in range(n):
    # Read the current and desired seats from the input
    current_seat, desired_seat = map(int, input().split())
    current_seats.append(current_seat)
    desired_seats.append(desired_seat)

# Call the count_seating_arrangements function and print the result
print(count_seating_arrangements(n, current_seats, desired_seats))

