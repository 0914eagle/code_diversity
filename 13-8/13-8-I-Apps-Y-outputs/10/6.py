
def get_best_days(forecast):
    # Find the two days with the lowest temperature
    min_temp_1, min_temp_2 = float('inf'), float('inf')
    day_1, day_2 = 0, 0
    for i, temp in enumerate(forecast):
        if temp < min_temp_1:
            min_temp_2 = min_temp_1
            day_2 = day_1
            min_temp_1 = temp
            day_1 = i
        elif temp < min_temp_2:
            min_temp_2 = temp
            day_2 = i
    
    # Return the best day to start the trip and the resulting maximum temperature during the two hiking days
    return day_1, min_temp_2

def main():
    n = int(input())
    forecast = list(map(int, input().split()))
    day, temp = get_best_days(forecast)
    print(day, temp)

if __name__ == '__main__':
    main()

