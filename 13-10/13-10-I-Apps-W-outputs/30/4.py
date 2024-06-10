
def count_pictures(r, c, n, k):
    # Initialize a 2D array to store the positions of the violas
    violas = [[0] * c for _ in range(r)]
    # Loop through the input and mark the positions of the violas
    for i in range(n):
        x, y = map(int, input().split())
        violas[x - 1][y - 1] = 1
    
    # Initialize a variable to store the number of pictures
    pictures = 0
    # Loop through the rows of the orchestra
    for i in range(r):
        # Loop through the columns of the orchestra
        for j in range(c):
            # If the current position is a viola, increment the number of pictures
            if violas[i][j] == 1:
                pictures += 1
    
    # Return the number of pictures
    return pictures

def main():
    # Read the input
    r, c, n, k = map(int, input().split())
    # Call the count_pictures function and print the result
    print(count_pictures(r, c, n, k))

if __name__ == '__main__':
    main()

