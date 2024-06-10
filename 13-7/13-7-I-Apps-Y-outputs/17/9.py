
def get_return_days(p, n):
    # Initialize a list to store the return days for each kid
    return_days = [0] * n
    
    # Iterate through the permutation p
    for i in range(n):
        # If the kid's book is returned to its owner, update the return day for that kid
        if p[i] == i + 1:
            return_days[i] = 1
    
    # Return the list of return days
    return return_days

def main():
    # Read the number of queries
    q = int(input())
    
    # Iterate through each query
    for _ in range(q):
        # Read the number of kids and the permutation p
        n = int(input())
        p = list(map(int, input().split()))
        
        # Get the return days for each kid
        return_days = get_return_days(p, n)
        
        # Print the return days for each kid
        print(*return_days)

if __name__ == '__main__':
    main()

