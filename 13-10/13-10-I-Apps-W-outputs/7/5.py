
def get_min_charges(citizens, burles):
    # Sort the citizens by their welfare in descending order
    citizens.sort(reverse=True)
    # Initialize the minimum number of burles to spend as 0
    min_charges = 0
    # Loop through the citizens and calculate the minimum number of burles to spend
    for i in range(len(citizens)):
        # Calculate the difference between the current citizen's welfare and the minimum welfare
        diff = citizens[i] - burles[i]
        # If the difference is positive, add the difference to the minimum number of burles to spend
        if diff > 0:
            min_charges += diff
    return min_charges

def main():
    # Read the number of citizens and their welfare from stdin
    n = int(input())
    citizens = list(map(int, input().split()))
    # Calculate the minimum number of burles to spend
    min_charges = get_min_charges(citizens, burles)
    # Print the minimum number of burles to spend
    print(min_charges)

if __name__ == '__main__':
    main()

