
def get_cables(n, x, c):
    # Initialize variables
    byteland_cables = 0
    berland_cables = 0
    total_cables = 0
    
    # Iterate through the cities
    for i in range(n):
        # If the current city is of type Byteland, calculate the distance to the next Byteland city
        if c[i] == "B":
            byteland_cables += x[i+1] - x[i]
        # If the current city is of type Berland, calculate the distance to the next Berland city
        elif c[i] == "R":
            berland_cables += x[i+1] - x[i]
        # If the current city is disputed, calculate the distance to the next city of any type
        else:
            total_cables += min(x[i+1] - x[i], x[i+1] - x[i-1])
    
    # Return the minimum total length of cables
    return byteland_cables + berland_cables + total_cables

def main():
    # Read the number of cities and the coordinates and types of the cities
    n = int(input())
    x = list(map(int, input().split()))
    c = list(input())
    
    # Call the get_cables function and print the result
    print(get_cables(n, x, c))

if __name__ == '__main__':
    main()

