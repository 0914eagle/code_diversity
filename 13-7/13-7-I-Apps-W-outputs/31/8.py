
def get_ball_order(n, throws):
    # Initialize a list to store the possible ball orders
    ball_orders = []
    
    # Iterate over each possible ball order
    for i in range(1, n + 1):
        # Add the current ball order to the list of possible orders
        ball_orders.append(i)
    
    # Iterate over each throw
    for throw in throws:
        # Get the two students who will participate in the throw
        student1, student2 = throw
        
        # Swap the balls between the two students
        ball1 = ball_orders[student1 - 1]
        ball2 = ball_orders[student2 - 1]
        ball_orders[student1 - 1] = ball2
        ball_orders[student2 - 1] = ball1
    
    # Return the number of distinct ball orders
    return len(set(ball_orders))

def main():
    # Read the input n and throws
    n, throws = map(int, input().split())
    throws = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    # Calculate the number of distinct ball orders
    result = get_ball_order(n, throws)
    
    # Print the result
    print(result % 1000000007)

if __name__ == '__main__':
    main()

