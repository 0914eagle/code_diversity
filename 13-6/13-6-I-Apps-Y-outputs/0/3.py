
def get_happiness_points(x):
    # Initialize a list to store the happiness points for each coin
    happiness_points = [0, 0, 0, 0, 0, 0]
    
    # Loop through the available coins and calculate the happiness points for each coin
    for i in range(6):
        coin_value = [500, 100, 50, 10, 5, 1][i]
        happiness_points[i] = x // coin_value
        x %= coin_value
    
    # Calculate the total happiness points by summing up the happiness points for each coin
    total_happiness_points = sum(happiness_points)
    
    return total_happiness_points

def main():
    x = int(input())
    print(get_happiness_points(x))

if __name__ == '__main__':
    main()

