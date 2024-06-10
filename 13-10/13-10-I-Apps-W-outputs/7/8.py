
def get_equal_welfare(citizens):
    # Sort the list of citizens in ascending order
    citizens.sort()
    # Initialize the minimum number of burles as 0
    min_burles = 0
    # Loop through the list of citizens
    for i in range(len(citizens)):
        # Calculate the difference between the current citizen and the previous citizen
        diff = citizens[i] - citizens[i - 1]
        # If the difference is greater than 0, add the difference to the minimum number of burles
        if diff > 0:
            min_burles += diff
    return min_burles

def main():
    # Read the number of citizens and their welfare from stdin
    n = int(input())
    citizens = list(map(int, input().split()))
    # Call the get_equal_welfare function and print the result
    print(get_equal_welfare(citizens))

if __name__ == '__main__':
    main()

