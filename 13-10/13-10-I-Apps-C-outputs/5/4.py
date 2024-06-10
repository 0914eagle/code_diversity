
def get_number_of_supported_stewards(n, steward_strengths):
    # Sort the steward strengths in ascending order
    sorted_steward_strengths = sorted(steward_strengths)

    # Initialize variables to keep track of the number of stewards supported and the current strength
    num_supported_stewards = 0
    current_strength = 0

    # Iterate through the sorted steward strengths
    for steward_strength in sorted_steward_strengths:
        # If the current strength is less than the steward strength, increment the number of supported stewards
        if current_strength < steward_strength:
            num_supported_stewards += 1

        # Update the current strength to the steward strength
        current_strength = steward_strength

    return num_supported_stewards

def main():
    n = int(input())
    steward_strengths = list(map(int, input().split()))
    print(get_number_of_supported_stewards(n, steward_strengths))

if __name__ == '__main__':
    main()

