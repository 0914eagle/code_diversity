
def get_number_of_ways_to_break_chocolate(n, pieces):
    # Initialize a variable to store the number of ways to break the chocolate
    number_of_ways = 0
    
    # Iterate over each piece in the chocolate bar
    for i in range(n):
        # If the current piece has a nut, check if the previous piece has a nut as well
        if pieces[i] == 1:
            # If the previous piece has a nut as well, continue to the next piece
            if i > 0 and pieces[i-1] == 1:
                continue
            # If the previous piece does not have a nut, check if the next piece has a nut
            elif i < n-1 and pieces[i+1] == 1:
                # If the next piece has a nut, continue to the next piece
                continue
            # If the previous and next pieces do not have nuts, increment the number of ways to break the chocolate
            else:
                number_of_ways += 1
    
    # Return the number of ways to break the chocolate
    return number_of_ways

def main():
    # Read the number of pieces in the chocolate bar and the pieces with nuts
    n = int(input())
    pieces = list(map(int, input().split()))
    
    # Calculate the number of ways to break the chocolate
    number_of_ways = get_number_of_ways_to_break_chocolate(n, pieces)
    
    # Print the number of ways to break the chocolate
    print(number_of_ways)

if __name__ == '__main__':
    main()

