
def get_best_days(forecast):
    # Initialize variables
    min_temp = 100
    best_days = []

    # Iterate through the forecast
    for i in range(len(forecast)):
        # Check if the temperature is less than the minimum temperature
        if forecast[i] < min_temp:
            # Update the minimum temperature and the best days
            min_temp = forecast[i]
            best_days = [i]
        # Check if the temperature is equal to the minimum temperature
        elif forecast[i] == min_temp:
            # Add the day to the list of best days
            best_days.append(i)

    # Return the best days and the minimum temperature
    return best_days, min_temp

def main():
    # Read the input
    n = int(input())
    forecast = list(map(int, input().split()))

    # Get the best days and the minimum temperature
    best_days, min_temp = get_best_days(forecast)

    # Print the output
    print(best_days[0], min_temp)

if __name__ == '__main__':
    main()

