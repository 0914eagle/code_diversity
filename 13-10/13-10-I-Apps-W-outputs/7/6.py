
def get_minimum_charges(citizens):
    # Sort the citizens by their welfare in ascending order
    citizens.sort()
    # Initialize the minimum charges to 0
    minimum_charges = 0
    # Loop through the citizens and calculate the minimum charges needed to equalize their welfare
    for i in range(len(citizens)):
        # Calculate the difference between the current citizen's welfare and the welfare of the previous citizen
        diff = citizens[i] - citizens[i-1]
        # If the difference is positive, add the difference to the minimum charges
        if diff > 0:
            minimum_charges += diff
    return minimum_charges

def main():
    # Read the number of citizens and their welfare from stdin
    n = int(input())
    citizens = list(map(int, input().split()))
    # Call the get_minimum_charges function and print the result
    print(get_minimum_charges(citizens))

if __name__ == '__main__':
    main()

