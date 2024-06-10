
def get_number_of_supported_stewards(stewards):
    # Sort the stewards in non-decreasing order
    stewards.sort()
    # Initialize the number of supported stewards to 0
    number_of_supported_stewards = 0
    # Iterate through the stewards
    for i in range(len(stewards)):
        # Check if there is a steward with strength less than the current steward
        if i > 0 and stewards[i] > stewards[i - 1]:
            # Increment the number of supported stewards
            number_of_supported_stewards += 1
        # Check if there is a steward with strength greater than the current steward
        if i < len(stewards) - 1 and stewards[i] < stewards[i + 1]:
            # Increment the number of supported stewards
            number_of_supported_stewards += 1
    # Return the number of supported stewards
    return number_of_supported_stewards

def main():
    # Read the number of stewards
    number_of_stewards = int(input())
    # Read the strengths of the stewards
    stewards = list(map(int, input().split()))
    # Find the number of supported stewards
    number_of_supported_stewards = get_number_of_supported_stewards(stewards)
    # Print the number of supported stewards
    print(number_of_supported_stewards)

if __name__ == '__main__':
    main()

