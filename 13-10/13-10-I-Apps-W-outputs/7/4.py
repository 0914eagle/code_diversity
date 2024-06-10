
def get_min_burles(citizen_welfare):
    # Sort the welfare of citizens in non-decreasing order
    citizen_welfare.sort()
    # Initialize the minimum number of burles as 0
    min_burles = 0
    # Loop through the citizens and calculate the minimum number of burles needed
    for i in range(len(citizen_welfare)):
        # Calculate the difference between the current citizen's welfare and the average welfare
        diff = citizen_welfare[i] - sum(citizen_welfare) / len(citizen_welfare)
        # If the difference is positive, add the difference to the minimum number of burles
        if diff > 0:
            min_burles += diff
    return min_burles

def main():
    # Read the number of citizens and their welfare from stdin
    n = int(input())
    citizen_welfare = list(map(int, input().split()))
    # Call the get_min_burles function to get the minimum number of burles needed
    min_burles = get_min_burles(citizen_welfare)
    # Print the minimum number of burles
    print(min_burles)

if __name__ == '__main__':
    main()

