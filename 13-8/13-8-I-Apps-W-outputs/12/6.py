
def read_notes(a, b):
    # Initialize variables
    n = 0
    m = 0
    p = []
    q = []
    
    # Loop through all possible values of n
    for i in range(1, a + 1):
        # Calculate the number of hours needed to read i notes in the first day
        hours_first_day = sum(range(1, i + 1))
        
        # Check if the number of hours needed to read i notes in the first day is less than or equal to a
        if hours_first_day <= a:
            # Calculate the number of hours needed to read (a - hours_first_day) notes in the second day
            hours_second_day = sum(range(1, a - hours_first_day + 1))
            
            # Check if the number of hours needed to read (a - hours_first_day) notes in the second day is less than or equal to b
            if hours_second_day <= b:
                # Update n and m
                n = i
                m = a - hours_first_day
                
                # Update p and q
                p = list(range(1, n + 1))
                q = list(range(1, m + 1))
                
                # Break out of the loop
                break
    
    # Return n, p, and q
    return n, p, q

def main():
    # Read a and b
    a, b = map(int, input().split())
    
    # Call the read_notes function
    n, p, q = read_notes(a, b)
    
    # Print the output
    print(n)
    print(*p)
    print(m)
    print(*q)

if __name__ == '__main__':
    main()

