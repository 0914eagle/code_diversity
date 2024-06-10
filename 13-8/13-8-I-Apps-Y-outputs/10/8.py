
def get_best_day_and_temp(forecast):
    # Initialize variables
    best_day = 0
    best_temp = 40
    current_temp = 0
    
    # Iterate through the forecast
    for i in range(len(forecast)):
        current_temp += forecast[i]
        if current_temp < best_temp:
            best_day = i
            best_temp = current_temp
    
    return best_day, best_temp

def main():
    n = int(input())
    forecast = list(map(int, input().split()))
    best_day, best_temp = get_best_day_and_temp(forecast)
    print(best_day, best_temp)

if __name__ == '__main__':
    main()

