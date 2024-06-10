
def get_best_days(forecast):
    # Initialize variables
    best_day = 0
    best_temp = 40
    second_best_day = 0
    second_best_temp = 40
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        # Check if the current day is the best day so far
        if forecast[i] < best_temp:
            # If so, update the best day and temperature
            best_day = i
            best_temp = forecast[i]
        # Check if the current day is the second best day so far
        if forecast[i] < second_best_temp:
            # If so, update the second best day and temperature
            second_best_day = i
            second_best_temp = forecast[i]
    
    # Return the best day and temperature
    return best_day, best_temp

def get_best_days_with_min_temp(forecast, min_temp):
    # Initialize variables
    best_day = 0
    best_temp = 40
    second_best_day = 0
    second_best_temp = 40
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        # Check if the current day is the best day so far
        if forecast[i] < best_temp and forecast[i] >= min_temp:
            # If so, update the best day and temperature
            best_day = i
            best_temp = forecast[i]
        # Check if the current day is the second best day so far
        if forecast[i] < second_best_temp and forecast[i] >= min_temp:
            # If so, update the second best day and temperature
            second_best_day = i
            second_best_temp = forecast[i]
    
    # Return the best day and temperature
    return best_day, best_temp

def main():
    # Read the forecast
    n = int(input())
    forecast = list(map(int, input().split()))
    
    # Get the best days
    best_day, best_temp = get_best_days(forecast)
    second_best_day, second_best_temp = get_best_days_with_min_temp(forecast, best_temp)
    
    # Print the results
    print(best_day, best_temp)
    print(second_best_day, second_best_temp)

if __name__ == '__main__':
    main()

