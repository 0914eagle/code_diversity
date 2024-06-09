
def count_ways(n, pieces):
    # Initialize the number of ways to be 0
    ways = 0
    
    # Iterate over each piece in the chocolate bar
    for i in range(n):
        # If the current piece has a nut
        if pieces[i] == 1:
            # Check if the previous piece has a nut
            if i > 0 and pieces[i-1] == 1:
                # If the previous piece has a nut, we can break the chocolate between the current piece and the previous piece
                ways += 1
            # Check if the next piece has a nut
            if i < n-1 and pieces[i+1] == 1:
                # If the next piece has a nut, we can break the chocolate between the current piece and the next piece
                ways += 1
    
    # Return the number of ways to break the chocolate
    return ways

def main():
    # Read the number of pieces in the chocolate bar
    n = int(input())
    # Read the pieces of the chocolate bar
    pieces = list(map(int, input().split()))
    # Calculate the number of ways to break the chocolate
    ways = count_ways(n, pieces)
    # Print the number of ways
    print(ways)

if __name__ == '__main__':
    main()

