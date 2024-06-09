
def get_happiness_points(x):
    # Initialize a list to store the happiness points for each coin
    happiness_points = [0, 0, 0, 0, 0, 0]
    
    # Calculate the happiness points for each coin
    for i in range(6):
        if i == 0:
            happiness_points[i] = x // 500
        elif i == 1:
            happiness_points[i] = x // 100
        elif i == 2:
            happiness_points[i] = x // 50
        elif i == 3:
            happiness_points[i] = x // 10
        elif i == 4:
            happiness_points[i] = x // 5
        else:
            happiness_points[i] = x
    
    # Calculate the total happiness points
    total_happiness_points = 0
    for i in range(6):
        total_happiness_points += happiness_points[i]
    
    return total_happiness_points

def main():
    x = int(input())
    print(get_happiness_points(x))

if __name__ == '__main__':
    main()

