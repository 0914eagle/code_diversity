
def get_max_days_eating(a, b, c):
    # Initialize variables
    max_days = 0
    days_eaten = 0
    day_of_week = 0
    
    # Iterate through all possible days of the week
    for i in range(1, 8):
        # Check if there is enough food for the current day
        if (i == 1 or i == 4 or i == 7) and a >= 1:
            a -= 1
            days_eaten += 1
        elif (i == 2 or i == 6) and b >= 1:
            b -= 1
            days_eaten += 1
        elif c >= 1:
            c -= 1
            days_eaten += 1
        else:
            break
        
        # Check if this is the longest streak so far
        if days_eaten > max_days:
            max_days = days_eaten
            day_of_week = i
    
    # Return the result
    return max_days, day_of_week

def main():
    a, b, c = map(int, input().split())
    max_days, day_of_week = get_max_days_eating(a, b, c)
    print(max_days)

if __name__ == '__main__':
    main()

