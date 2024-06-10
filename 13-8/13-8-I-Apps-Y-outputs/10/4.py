
def get_best_days(temperatures):
    # Find the two days with the lowest maximum temperatures
    day_1, day_2 = sorted(range(len(temperatures)), key=lambda i: temperatures[i])[:2]
    
    # Return the best day to start the trip and the maximum temperature during the two hiking days
    return day_1, max(temperatures[day_1:day_1+2])

def main():
    n = int(input())
    temperatures = [int(i) for i in input().split()]
    print(*get_best_days(temperatures))

if __name__ == '__main__':
    main()

