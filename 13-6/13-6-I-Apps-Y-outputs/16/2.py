
def get_first_return_days(p, n):
    # Initialize a list to store the first return days for each kid
    first_return_days = [0] * n
    
    # Iterate through each day
    for day in range(1, n + 1):
        # Iterate through each kid
        for kid in range(n):
            # If the kid's book is returned to him, update the first return day
            if p[kid] == kid:
                first_return_days[kid] = day
                break
    
    return first_return_days

def main():
    # Read the number of queries
    q = int(input())
    
    # Iterate through each query
    for _ in range(q):
        # Read the number of kids and the permutation
        n = int(input())
        p = list(map(int, input().split()))
        
        # Get the first return days for each kid
        first_return_days = get_first_return_days(p, n)
        
        # Print the first return days
        print(*first_return_days)

if __name__ == '__main__':
    main()

