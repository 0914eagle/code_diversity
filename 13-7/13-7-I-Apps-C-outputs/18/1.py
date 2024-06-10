
def get_max_executives(briefcases):
    # Sort the briefcases in non-decreasing order
    briefcases.sort()
    # Initialize the number of executives to be rewarded as 0
    num_executives = 0
    # Initialize the total number of bananas to be 0
    total_bananas = 0
    # Iterate through the briefcases
    for briefcase in briefcases:
        # If the total number of bananas plus the number of bananas in the current briefcase is less than or equal to the number of executives, add the number of bananas in the current briefcase to the total and increment the number of executives
        if total_bananas + briefcase <= num_executives:
            total_bananas += briefcase
            num_executives += 1
        # Otherwise, add the number of bananas in the current briefcase to the total and break out of the loop
        else:
            total_bananas += briefcase
            break
    # Return the maximum number of executives that can be rewarded
    return num_executives

def main():
    # Read the number of briefcases and the number of bananas in each briefcase from stdin
    num_briefcases = int(input())
    briefcases = list(map(int, input().split()))
    # Call the get_max_executives function and print the result
    print(get_max_executives(briefcases))

if __name__ == '__main__':
    main()

