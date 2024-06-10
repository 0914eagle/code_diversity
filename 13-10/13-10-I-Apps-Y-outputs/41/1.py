
def get_days_to_eat_without_food_purchases(a, b, c):
    # Initialize a list to store the number of days the cat can eat without additional food purchases for each day of the week
    days_to_eat_without_food_purchases = [0, 0, 0, 0, 0, 0, 0]
    
    # Iterate over the days of the week
    for day in range(7):
        # Check if the cat can eat fish food on the current day
        if day in [0, 3, 6] and a > 0:
            # The cat can eat fish food on the current day, so increment the number of days the cat can eat without additional food purchases
            days_to_eat_without_food_purchases[day] += 1
            # Decrement the number of fish food rations in the backpack
            a -= 1
        
        # Check if the cat can eat rabbit stew on the current day
        if day in [1, 4, 5] and b > 0:
            # The cat can eat rabbit stew on the current day, so increment the number of days the cat can eat without additional food purchases
            days_to_eat_without_food_purchases[day] += 1
            # Decrement the number of rabbit stew rations in the backpack
            b -= 1
        
        # Check if the cat can eat chicken stake on the current day
        if day in [2, 3, 5] and c > 0:
            # The cat can eat chicken stake on the current day, so increment the number of days the cat can eat without additional food purchases
            days_to_eat_without_food_purchases[day] += 1
            # Decrement the number of chicken stake rations in the backpack
            c -= 1
    
    # Return the maximum number of days the cat can eat without additional food purchases
    return max(days_to_eat_without_food_purchases)

def main():
    # Read the number of fish food, rabbit stew and chicken stake rations in Polycarp's backpack from stdin
    a, b, c = map(int, input().split())
    
    # Call the get_days_to_eat_without_food_purchases function and print the result
    print(get_days_to_eat_without_food_purchases(a, b, c))

if __name__ == '__main__':
    main()

