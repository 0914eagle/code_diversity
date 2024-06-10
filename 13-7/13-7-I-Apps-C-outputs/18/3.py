
def get_maximum_executives(briefcases):
    # Sort the briefcases in non-decreasing order
    briefcases.sort()
    # Initialize the number of executives to be rewarded
    num_executives = 0
    # Initialize the total number of bananas to be rewarded
    total_bananas = 0
    # Loop through the briefcases
    for briefcase in briefcases:
        # If the total number of bananas plus the number of bananas in the current briefcase is less than or equal to the number of bananas in the previous briefcase,
        # then the current briefcase can be given to the current executive
        if total_bananas + briefcase <= briefcases[num_executives]:
            # Increment the number of executives to be rewarded
            num_executives += 1
            # Add the number of bananas in the current briefcase to the total number of bananas to be rewarded
            total_bananas += briefcase
        # Otherwise, the current briefcase cannot be given to the current executive
        else:
            # Break out of the loop
            break
    # Return the maximum number of executives that can be rewarded
    return num_executives

def main():
    # Read the number of briefcases
    num_briefcases = int(input())
    # Read the number of bananas in each briefcase
    briefcases = list(map(int, input().split()))
    # Get the maximum number of executives that can be rewarded
    max_executives = get_maximum_executives(briefcases)
    # Print the maximum number of executives that can be rewarded
    print(max_executives)

if __name__ == '__main__':
    main()

