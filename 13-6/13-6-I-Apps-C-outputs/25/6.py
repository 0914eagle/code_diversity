
def solve(n, t, photographs):
    # Sort the photographs by their earliest starting time
    photographs.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through each photograph
    for photograph in photographs:
        # Check if the photograph can be taken at the current time
        if current_time + t <= photograph[1]:
            # Take the photograph and update the current time
            current_time += t
        else:
            # The photograph cannot be taken at the current time, return "no"
            return "no"

    # If all photographs were taken, return "yes"
    return "yes"

