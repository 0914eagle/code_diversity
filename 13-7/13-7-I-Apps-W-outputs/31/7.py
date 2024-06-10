
def get_distinct_ball_orders(n, throws):
    # Initialize a list to store the number of distinct ball orders
    distinct_orders = 1
    
    # Iterate over the throws
    for throw in throws:
        # Get the number of students who can participate in this throw
        num_students = len(throw)
        
        # Calculate the number of distinct ball orders after this throw
        distinct_orders *= num_students ** n
        
        # Calculate the number of duplicates after this throw
        duplicates = 1
        for i in range(num_students):
            duplicates *= (n - i)
        
        # Subtract the number of duplicates from the total number of distinct orders
        distinct_orders -= duplicates
    
    # Return the number of distinct ball orders modulo 1000000007
    return distinct_orders % 1000000007

def main():
    n = int(input())
    throws = [list(map(int, input().split())) for _ in range(n)]
    print(get_distinct_ball_orders(n, throws))

if __name__ == '__main__':
    main()

