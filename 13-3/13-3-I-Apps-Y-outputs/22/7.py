
def get_num_ways(N, A, x):
    # Calculate the sum of the integers on the cards
    sum_x = sum(x)
    # Calculate the average of the integers on the cards
    avg_x = sum_x / N
    # Calculate the difference between the average and the target average
    diff = abs(avg_x - A)
    # Initialize the number of ways to select cards to 0
    num_ways = 0
    # Loop through each card and check if the average of the selected cards is equal to the target average
    for i in range(N):
        # Calculate the sum of the integers on the selected cards
        sum_selected = sum(x[:i+1])
        # Calculate the average of the integers on the selected cards
        avg_selected = sum_selected / (i+1)
        # Check if the average of the selected cards is equal to the target average
        if abs(avg_selected - A) <= diff:
            # Increment the number of ways to select cards
            num_ways += 1
    # Return the number of ways to select cards
    return num_ways

def main():
    # Read the input from stdin
    N, A = map(int, input().split())
    x = list(map(int, input().split()))
    # Call the function to get the number of ways to select cards
    num_ways = get_num_ways(N, A, x)
    # Print the number of ways to select cards
    print(num_ways)

if __name__ == '__main__':
    main()

