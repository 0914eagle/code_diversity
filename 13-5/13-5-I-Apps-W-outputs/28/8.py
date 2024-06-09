
def number_of_ways_to_fill_tiles(n):
    # Initialize a list to store the number of ways to fill each row
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Loop through each row
    for i in range(1, n + 1):
        # Loop through each column in the current row
        for j in range(i + 1):
            # If the current cell is not in the last column, add the number of ways to fill the cell from the left and the cell above
            if j < i:
                ways[i] += ways[j] + ways[i - j - 1]
            # If the current cell is in the last column, add the number of ways to fill the cell from the left
            else:
                ways[i] += ways[j]
    
    # Return the number of ways to fill the last row
    return ways[n]

def main():
    n = int(input())
    print(number_of_ways_to_fill_tiles(n))

if __name__ == '__main__':
    main()

