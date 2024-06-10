
def get_max_days_without_purchases(a, b, c):
    # Initialize variables
    fish_days = [0, 1, 4]
    rabbit_days = [1, 2, 5, 6]
    chicken_days = [2, 3, 4, 5, 6]
    max_days = 0
    current_day = 0
    
    # Iterate through all possible starting days
    for i in range(7):
        # Initialize variables for current day
        fish_count = a
        rabbit_count = b
        chicken_count = c
        current_day += 1
        
        # Iterate through all possible days of the week
        for j in range(7):
            # Check if it is a fish day
            if j in fish_days:
                # If it is a fish day, consume a portion of fish food
                if fish_count > 0:
                    fish_count -= 1
                # If there is no more fish food, break the loop
                else:
                    break
            # Check if it is a rabbit day
            elif j in rabbit_days:
                # If it is a rabbit day, consume a portion of rabbit stew
                if rabbit_count > 0:
                    rabbit_count -= 1
                # If there is no more rabbit stew, break the loop
                else:
                    break
            # Check if it is a chicken day
            elif j in chicken_days:
                # If it is a chicken day, consume a portion of chicken stakes
                if chicken_count > 0:
                    chicken_count -= 1
                # If there is no more chicken stakes, break the loop
                else:
                    break
            
            # Increment the current day
            current_day += 1
        
        # If the current day is greater than the maximum day, update the maximum day
        if current_day > max_days:
            max_days = current_day
    
    # Return the maximum number of days without purchases
    return max_days

def main():
    a, b, c = map(int, input().strip().split())
    result = get_max_days_without_purchases(a, b, c)
    print(result)

if __name__ == '__main__':
    main()

