
def number_of_ways_to_break_chocolate(n, pieces):
    # Initialize a variable to store the number of ways
    num_ways = 0
    
    # Iterate over each piece in the chocolate bar
    for i in range(n):
        # If the current piece has a nut
        if pieces[i] == 1:
            # Increment the number of ways
            num_ways += 1
            # If the current piece is not the last piece in the bar
            if i != n - 1:
                # Increment the number of ways by the number of ways to break the chocolate bar after the current piece
                num_ways += number_of_ways_to_break_chocolate(n - i - 1, pieces[i + 1:])
    
    return num_ways

def main():
    # Read the number of pieces in the chocolate bar
    n = int(input())
    # Read the pieces of the chocolate bar
    pieces = list(map(int, input().split()))
    # Calculate the number of ways to break the chocolate bar
    num_ways = number_of_ways_to_break_chocolate(n, pieces)
    # Print the number of ways
    print(num_ways)

if __name__ == '__main__':
    main()

