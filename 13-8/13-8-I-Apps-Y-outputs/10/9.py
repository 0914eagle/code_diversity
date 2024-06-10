
def get_best_days(forecast):
    # Initialize variables
    best_days = []
    best_temp = 100
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        # Check if the temperature on the current day is less than the best temperature
        if forecast[i] < best_temp:
            # If it is, add the current day to the best days list and update the best temperature
            best_days.append(i)
            best_temp = forecast[i]
    
    # Return the best days and the corresponding temperature
    return best_days, best_temp

def get_start_day(forecast):
    # Get the best days and temperature
    best_days, best_temp = get_best_days(forecast)
    
    # If there is only one best day, return it
    if len(best_days) == 1:
        return best_days[0]
    
    # If there are multiple best days, return the smallest one
    return min(best_days)

if __name__ == '__main__':
    # Read the input
    n = int(input())
    forecast = [int(x) for x in input().split()]
    
    # Get the start day and the corresponding temperature
    start_day = get_start_day(forecast)
    temp = forecast[start_day]
    
    # Print the output
    print(start_day, temp)

