
def get_min_days(n, p, q, a, b):
    # Initialize variables
    days = 0
    exp = 0
    money = 0
    
    # Loop through each project
    for i in range(n):
        # Calculate the number of days needed for each project
        days_needed = (p - exp) / a[i]
        days_needed = int(days_needed) + 1 if days_needed % 1 != 0 else int(days_needed)
        
        # Calculate the experience and money gained from working on the project
        exp += a[i] * days_needed
        money += b[i] * days_needed
        
        # Check if the required experience and money have been gained
        if exp >= p and money >= q:
            return days
        
        # Update the number of days
        days += days_needed
    
    # If the required experience and money have not been gained, return -1
    return -1

def main():
    n, p, q = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(get_min_days(n, p, q, a, b))

if __name__ == '__main__':
    main()

