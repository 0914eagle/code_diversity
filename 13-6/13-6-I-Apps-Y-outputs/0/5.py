
def get_happiness_points(x):
    # Initialize a list to store the number of happiness points for each coin
    happiness_points = [0, 0, 0, 0, 0, 0]
    
    # Calculate the number of happiness points for each coin
    for i in range(6):
        coin_value = [500, 100, 50, 10, 5, 1][i]
        happiness_points[i] = x // coin_value
        x %= coin_value
    
    # Calculate the total number of happiness points
    total_happiness_points = 0
    for i in range(6):
        total_happiness_points += happiness_points[i] * [1000, 500, 200, 100, 50, 5][i]
    
    return total_happiness_points

def main():
    x = int(input())
    print(get_happiness_points(x))

if __name__ == '__main__':
    main()

