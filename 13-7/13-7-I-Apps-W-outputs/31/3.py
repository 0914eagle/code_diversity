
def get_ball_orders(n, throws):
    # Initialize a list to store the ball orders
    ball_orders = []
    
    # Base case: if there are no throws, return the initial order
    if not throws:
        return [list(range(1, n + 1))]
    
    # Recursive case: try all possible throws and combine the results
    for i in range(n):
        for j in range(i + 1, n):
            if throws[i] > 0 and throws[j] > 0:
                # Make the throw and recursively find the ball orders after that throw
                throws[i] -= 1
                throws[j] -= 1
                ball_orders += get_ball_orders(n, throws)
                throws[i] += 1
                throws[j] += 1
    
    # Return the list of ball orders
    return ball_orders

def main():
    n = int(input())
    throws = list(map(int, input().split()))
    print(get_ball_orders(n, throws) % 1000000007)

if __name__ == '__main__':
    main()

