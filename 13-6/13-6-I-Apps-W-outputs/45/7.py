
def count_ways(n, pieces):
    # Initialize the number of ways to break the chocolate to 0
    ways = 0
    
    # Loop through each piece in the chocolate bar
    for i in range(n):
        # If the current piece has a nut, check if the previous piece also has a nut
        if pieces[i] == 1 and (i == 0 or pieces[i-1] == 1):
            # If the previous piece also has a nut, continue to the next piece
            continue
        # If the current piece has a nut and the previous piece does not have a nut, or if the current piece is the first piece and it has a nut, increment the number of ways
        ways += 1
    
    # Return the number of ways to break the chocolate
    return ways

def main():
    # Read the number of pieces in the chocolate bar and the pieces with nuts
    n = int(input())
    pieces = list(map(int, input().split()))
    
    # Call the count_ways function and print the number of ways to break the chocolate
    print(count_ways(n, pieces))

if __name__ == '__main__':
    main()

