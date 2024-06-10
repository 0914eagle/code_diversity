
def get_best_day_and_temp(forecast):
    # Initialize variables
    best_day = 0
    best_temp = 0
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        # Calculate the maximum temperature for the two hiking days starting on day i
        temp = max(forecast[i], forecast[i+1])
        
        # If the temperature is lower than the current best temperature, update the best day and temperature
        if temp < best_temp:
            best_day = i
            best_temp = temp
    
    # Return the best day and temperature
    return best_day, best_temp

def main():
    # Read the input
    n = int(input())
    forecast = list(map(int, input().split()))
    
    # Get the best day and temperature
    best_day, best_temp = get_best_day_and_temp(forecast)
    
    # Print the output
    print(best_day, best_temp)

if __name__ == '__main__':
    main()

