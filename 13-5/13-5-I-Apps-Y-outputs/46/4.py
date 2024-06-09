
def get_max_consecutive_rainy_days(weather_records):
    max_consecutive_rainy_days = 0
    current_consecutive_rainy_days = 0
    for i in range(len(weather_records)):
        if weather_records[i] == "R":
            current_consecutive_rainy_days += 1
        else:
            if current_consecutive_rainy_days > max_consecutive_rainy_days:
                max_consecutive_rainy_days = current_consecutive_rainy_days
            current_consecutive_rainy_days = 0
    
    if current_consecutive_rainy_days > max_consecutive_rainy_days:
        max_consecutive_rainy_days = current_consecutive_rainy_days
    
    return max_consecutive_rainy_days

def main():
    weather_records = input()
    print(get_max_consecutive_rainy_days(weather_records))

if __name__ == '__main__':
    main()

