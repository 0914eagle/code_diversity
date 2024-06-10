
def get_days_to_eat(fish, rabbit, chicken):
    # Initialize variables
    days = 0
    fish_days = [1, 3, 7]
    rabbit_days = [2, 6]
    chicken_days = [4, 5]
    
    # Loop through each day of the week
    for day in range(1, 8):
        # Check if there is enough food for the current day
        if day in fish_days and fish > 0:
            fish -= 1
        elif day in rabbit_days and rabbit > 0:
            rabbit -= 1
        elif day in chicken_days and chicken > 0:
            chicken -= 1
        else:
            # If there is no food for the current day, break the loop
            break
        
        # Increment the number of days the cat can eat
        days += 1
    
    # Return the number of days the cat can eat
    return days

def main():
    # Read the input
    fish, rabbit, chicken = map(int, input().split())
    
    # Calculate the number of days the cat can eat
    days = get_days_to_eat(fish, rabbit, chicken)
    
    # Print the result
    print(days)

if __name__ == '__main__':
    main()

