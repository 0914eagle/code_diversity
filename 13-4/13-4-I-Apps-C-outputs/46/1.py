
def get_min_days(n, p, q, a, b):
    # Initialize variables
    days = 0
    exp = 0
    money = 0
    
    # Loop through each project
    for i in range(n):
        # Calculate the number of days needed for this project
        days_needed = (p - exp) / a[i]
        days_needed = max(days_needed, (q - money) / b[i])
        
        # Update the number of days and experience and money
        days += days_needed
        exp += a[i] * days_needed
        money += b[i] * days_needed
    
    # Return the minimum number of days needed
    return days

def main():
    # Read input
    n, p, q = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # Calculate the minimum number of days
    days = get_min_days(n, p, q, a, b)
    
    # Print output
    print(days)

if __name__ == '__main__':
    main()

