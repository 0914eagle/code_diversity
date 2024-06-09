
def get_max_consecutive_rainy_days(weather_record):
    max_consecutive_rainy_days = 0
    current_consecutive_rainy_days = 0
    for day in weather_record:
        if day == "R":
            current_consecutive_rainy_days += 1
        else:
            max_consecutive_rainy_days = max(max_consecutive_rainy_days, current_consecutive_rainy_days)
            current_consecutive_rainy_days = 0
    return max(max_consecutive_rainy_days, current_consecutive_rainy_days)

def main():
    weather_record = input()
    print(get_max_consecutive_rainy_days(weather_record))

if __name__ == '__main__':
    main()

