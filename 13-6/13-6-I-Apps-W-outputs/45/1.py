
def count_ways(n, pieces):
    # Initialize the number of ways to 0
    ways = 0
    
    # Loop through each piece and check if it contains a nut
    for i in range(n):
        # If the current piece contains a nut, check if the previous piece contains a nut as well
        if pieces[i] == 1 and (i == 0 or pieces[i-1] == 1):
            # If the previous piece also contains a nut, we can break the chocolate between the current piece and the previous piece
            ways += 1
    
    # Return the number of ways to break the chocolate
    return ways

def main():
    # Read the number of pieces and the pieces information from stdin
    n = int(input())
    pieces = list(map(int, input().split()))
    
    # Call the count_ways function and print the result
    print(count_ways(n, pieces))

if __name__ == '__main__':
    main()

