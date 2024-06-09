
import math

def get_flavor(apples):
    # Calculate the sum of the flavors of all apples
    total_flavor = sum(apples)

    # Sort the apples in ascending order of their flavors
    apples.sort()

    # Initialize the minimum difference between the flavors of the apple pie made of all apples and the apple pie made of the remaining N-1 apples
    min_diff = math.inf

    # Loop through each apple and calculate the difference between the flavors of the apple pie made of all apples and the apple pie made of the remaining N-1 apples
    for i in range(len(apples)):
        # Calculate the flavor of the apple pie made of the remaining N-1 apples
        remaining_flavor = total_flavor - apples[i]

        # Calculate the difference between the flavors of the apple pie made of all apples and the apple pie made of the remaining N-1 apples
        diff = abs(remaining_flavor - total_flavor)

        # Update the minimum difference if the current difference is smaller than the minimum difference
        if diff < min_diff:
            min_diff = diff

    # Return the flavor of the apple pie made of the remaining N-1 apples
    return remaining_flavor

n, l = map(int, input().split())
apples = list(map(int, input().split()))

# Print the flavor of the apple pie made of the remaining N-1 apples
print(get_flavor(apples))

