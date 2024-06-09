
def get_happiness_points(x):
    # Initialize a list to store the happiness points for each coin
    happiness_points = [0, 0, 0, 0, 0, 0]
    
    # Calculate the happiness points for each coin
    for i in range(6):
        happiness_points[i] = x // (500 - i * 50)
        x %= (500 - i * 50)
    
    # Return the maximum happiness points
    return max(happiness_points)

def main():
    x = int(input())
    print(get_happiness_points(x))

if __name__ == '__main__':
    main()

