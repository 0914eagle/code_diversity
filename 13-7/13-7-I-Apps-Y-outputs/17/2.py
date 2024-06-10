
def get_return_days(n, p):
    # Initialize a list to store the return days for each kid
    return_days = [0] * n
    
    # Iterate through each day
    for day in range(1, n + 1):
        # Iterate through each kid
        for kid in range(n):
            # If the kid's book is returned to him, update the return day
            if p[kid] == kid:
                return_days[kid] = day
    
    return return_days

def main():
    # Read the number of queries
    q = int(input())
    
    # Iterate through each query
    for _ in range(q):
        # Read the number of kids and the permutation
        n = int(input())
        p = list(map(int, input().split()))
        
        # Get the return days for each kid
        return_days = get_return_days(n, p)
        
        # Print the return days
        print(*return_days)

if __name__ == '__main__':
    main()

