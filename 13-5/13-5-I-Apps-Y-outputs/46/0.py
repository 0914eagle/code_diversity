
def get_consecutive_rainy_days(weather_record):
    consecutive_rainy_days = 0
    for i in range(len(weather_record)):
        if weather_record[i] == "R":
            consecutive_rainy_days += 1
        else:
            consecutive_rainy_days = 0
    return consecutive_rainy_days

def main():
    weather_record = input()
    print(get_consecutive_rainy_days(weather_record))

if __name__ == '__main__':
    main()

