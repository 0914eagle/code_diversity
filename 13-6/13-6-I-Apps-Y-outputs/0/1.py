
def get_maximum_happiness_points(x):
    # Initialize a list to store the maximum happiness points for each coin
    max_happiness_points = [0] * 6

    # Loop through each coin and calculate the maximum happiness points
    for i in range(6):
        # Calculate the number of coins that can be obtained for the current coin
        num_coins = x // coin_values[i]

        # Calculate the happiness points for the current coin
        happiness_points = num_coins * (coin_values[i] // 5) * 1000 + num_coins * (coin_values[i] % 5) * 5

        # Update the maximum happiness points for the current coin
        max_happiness_points[i] = happiness_points

    # Return the maximum happiness points among all coins
    return max(max_happiness_points)

def main():
    x = int(input())
    print(get_maximum_happiness_points(x))

if __name__ == '__main__':
    main()

