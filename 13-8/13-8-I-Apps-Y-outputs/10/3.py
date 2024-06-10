
def get_best_days(forecast):
    # Initialize variables
    best_day = 0
    best_temp = 100
    second_best_day = 0
    second_best_temp = 100
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        # Check if the temperature on this day is lower than the best temperature
        if forecast[i] < best_temp:
            # If it is, update the best temperature and day
            best_temp = forecast[i]
            best_day = i
        # Check if the temperature on this day is lower than the second-best temperature
        if forecast[i] < second_best_temp:
            # If it is, update the second-best temperature and day
            second_best_temp = forecast[i]
            second_best_day = i
    
    # Return the best day and temperature
    return best_day, best_temp

def get_second_best_days(forecast):
    # Initialize variables
    second_best_day = 0
    second_best_temp = 100
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        # Check if the temperature on this day is lower than the second-best temperature
        if forecast[i] < second_best_temp:
            # If it is, update the second-best temperature and day
            second_best_temp = forecast[i]
            second_best_day = i
    
    # Return the second-best day and temperature
    return second_best_day, second_best_temp

if __name__ == '__main__':
    # Read the input
    n = int(input())
    forecast = list(map(int, input().split()))
    
    # Call the functions
    best_day, best_temp = get_best_days(forecast)
    second_best_day, second_best_temp = get_second_best_days(forecast)
    
    # Print the output
    print(best_day, best_temp)
    print(second_best_day, second_best_temp)

