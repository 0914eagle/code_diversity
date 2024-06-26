
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
            # Update the best day and temperature
            best_day = i
            best_temp = forecast[i]
        # Check if the current day is the second best day so far
        if forecast[i] < second_best_temp:
            # Update the second best day and temperature
            second_best_day = i
            second_best_temp = forecast[i]
    
    # Return the best day and temperature
    return best_day, best_temp

def get_output(forecast):
    # Get the best days for the trip
    best_day, best_temp = get_best_days(forecast)
    
    # Print the output
    print(f"The best day to start the trip is day {best_day + 1} with a maximum temperature of {best_temp}.")

if __name__ == '__main__':
    # Get the forecast
    forecast = list(map(int, input().split()))
    
    # Get the output
    get_output(forecast)

