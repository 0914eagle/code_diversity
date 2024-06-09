
def get_max_happiness_points(x):
    # Initialize a list to store the number of happiness points for each coin
    happiness_points = [0, 5, 10, 50, 100, 500]
    
    # Initialize a list to store the number of coins for each denomination
    num_coins = [0, 0, 0, 0, 0, 0]
    
    # Calculate the number of coins for each denomination
    for i in range(len(happiness_points)):
        num_coins[i] = x // happiness_points[i]
        x %= happiness_points[i]
    
    # Calculate the total number of happiness points
    total_happiness_points = 0
    for i in range(len(happiness_points)):
        total_happiness_points += happiness_points[i] * num_coins[i]
    
    return total_happiness_points

def main():
    x = int(input())
    print(get_max_happiness_points(x))

if __name__ == '__main__':
    main()

