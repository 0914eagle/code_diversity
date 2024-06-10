
def get_distinct_ball_orders(n, throws):
    # Initialize a list to store the number of distinct ball orders
    distinct_orders = 1
    
    # Iterate over the throws
    for i in range(n):
        # Calculate the number of distinct ball orders after the current throw
        distinct_orders *= throws[i]
        
        # Calculate the number of repeated ball orders after the current throw
        repeated_orders = throws[i] - 1
        
        # Subtract the number of repeated ball orders from the total number of distinct orders
        distinct_orders -= repeated_orders
        
        # Modulo the result by 1000000007 to avoid overflow
        distinct_orders %= 1000000007
    
    return distinct_orders

def main():
    n = int(input())
    throws = list(map(int, input().split()))
    print(get_distinct_ball_orders(n, throws))

if __name__ == '__main__':
    main()

