
def get_max_days(a, b, c):
    # Initialize variables
    max_days = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Iterate through each day of the week
    for day in days:
        # Check if the day is a fish food day
        if day in ["Monday", "Thursday", "Sunday"]:
            # If the day is a fish food day, check if there are enough fish food rations
            if a >= 1:
                # If there are enough fish food rations, increment the max days variable
                max_days += 1
                # Decrement the number of fish food rations
                a -= 1
            else:
                # If there are not enough fish food rations, break the loop
                break
        # Check if the day is a rabbit stew day
        elif day in ["Tuesday", "Saturday"]:
            # If the day is a rabbit stew day, check if there are enough rabbit stew rations
            if b >= 1:
                # If there are enough rabbit stew rations, increment the max days variable
                max_days += 1
                # Decrement the number of rabbit stew rations
                b -= 1
            else:
                # If there are not enough rabbit stew rations, break the loop
                break
        # Check if the day is a chicken stake day
        else:
            # If the day is a chicken stake day, check if there are enough chicken stake rations
            if c >= 1:
                # If there are enough chicken stake rations, increment the max days variable
                max_days += 1
                # Decrement the number of chicken stake rations
                c -= 1
            else:
                # If there are not enough chicken stake rations, break the loop
                break
    
    # Return the maximum number of days the cat can eat in a trip without additional food purchases
    return max_days

def main():
    a, b, c = map(int, input().split())
    print(get_max_days(a, b, c))

if __name__ == '__main__':
    main()

