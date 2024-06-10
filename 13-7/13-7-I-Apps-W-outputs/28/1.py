
def count_ways(field):
    # Initialize the number of ways to fill the empty cells
    num_ways = 1
    
    # Iterate over the field
    for i in range(len(field)):
        # If the current cell is empty
        if field[i] == "?":
            # Count the number of ways to fill the cell with a bomb
            num_ways *= 2
        # If the current cell contains a number
        elif field[i].isdigit():
            # Count the number of ways to fill the cell with a bomb
            num_ways *= int(field[i]) + 1
    
    # Return the number of ways modulo 1000000007
    return num_ways % 1000000007

def main():
    field = input()
    print(count_ways(field))

if __name__ == '__main__':
    main()

